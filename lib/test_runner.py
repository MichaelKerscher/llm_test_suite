# lib/test_runner.py
import os
import time
import json
import re
from dotenv import load_dotenv

from lib.logger import log_response
from lib.clients import CLIENTS

import lib.context_policy_s2 as s2
import lib.context_policy_signal as s2_signal

load_dotenv()

ENABLE_JUDGE_DEFAULT = os.getenv("TESTSUITE_ENABLE_JUDGE", "true").lower() == "true"
RUN_MODE_DEFAULT = os.getenv("TESTSUITE_RUN_MODE", "incident").lower()  # testcase|incident

# Separate result trees per judging protocol: the single-testcase runs must not
# accumulate into the directories holding the incident-group runs, since the two
# are not comparable and _next_run_index() would interleave them.
RESULTS_ROOT = os.getenv("TESTSUITE_RESULTS_ROOT", "results")


def _normalize_client_name(name: str) -> str:
    name = (name or "").strip().lower()
    if name in ("506", "506.ai", "companygpt", "company_gpt", "companygpt_506"):
        return "506"
    return name or "unknown"


def _result_dir_for_client(client_name: str, model: str = "") -> str:
    model_slug = (model or "unknown").replace(":", "-").replace("/", "-")
    return f"{RESULTS_ROOT}/{client_name}/{model_slug}"


def _safe_json_dumps(obj) -> str:
    return json.dumps(obj, ensure_ascii=False)


def _final_prompt_for_log(client, prompt: str, context: dict | None) -> str:
    """
    Reconstructs the prompt as the client actually composes it, so that the
    log contains the string sent to the model rather than the pre-injection
    user message. Falls back to the bare prompt if a client does not expose
    context injection.
    """
    fn = getattr(client, "append_context_to_prompt", None)
    if callable(fn):
        try:
            return fn(prompt, context)
        except Exception:
            return prompt
    return prompt


def _is_client_error_answer(answer) -> bool:
    """
    companygpt_client.generate() swallows exceptions and returns them as the
    answer string. Without this check a failed request would be logged as a
    successful response and scored by the judge.
    """
    return isinstance(answer, str) and answer.startswith(
        ("[CompanyGPT ERROR]", "[CompanyGPT]", "[CompanyGPT JUDGE ERROR]")
    )


# ----------------------------
# Judge JSON robustness helpers
# ----------------------------
def _sanitize_judge_jsonish(text: str) -> str:
    """
    Makes 'almost JSON' from LLM outputs parseable:
    - fixes mojibake smart quotes
    - normalizes unicode quotes
    - removes BOM
    - removes common trailing commas before } or ]
    """
    if not isinstance(text, str):
        return text

    s = text.strip().lstrip("\ufeff")

    replacements = {
        # mojibake quotes
        "â€ž": '"', "â€œ": '"', "â€": '"',
        "â€™": "'", "â€˜": "'",
        # real unicode quotes
        "\u201c": '"', "\u201d": '"', "\u201e": '"',
        "\u2018": "'", "\u2019": "'",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)

    # common trailing commas: { ... ,} or [ ... ,]
    s = re.sub(r",(\s*[}\]])", r"\1", s)

    return s


def _extract_first_json_array(text: str) -> str | None:
    if not isinstance(text, str):
        return None
    s = text.strip()
    l = s.find("[")
    r = s.rfind("]")
    if l != -1 and r != -1 and r > l:
        return s[l : r + 1]
    return None


def _extract_first_json_object(text: str) -> str | None:
    if not isinstance(text, str):
        return None
    s = text.strip()
    l = s.find("{")
    r = s.rfind("}")
    if l != -1 and r != -1 and r > l:
        return s[l : r + 1]
    return None


def _repair_unescaped_quotes_in_json_strings(s: str) -> str:
    """
    Heuristic repair for invalid JSON produced by LLMs:
    replaces unescaped " inside JSON string literals with apostrophes ',
    so that json.loads() succeeds.
    """
    if not isinstance(s, str) or '"' not in s:
        return s

    out: list[str] = []
    in_str = False
    esc = False
    i = 0
    n = len(s)

    def looks_like_string_end(idx: int) -> bool:
        j = idx + 1
        while j < n and s[j] in " \t\r\n":
            j += 1
        if j >= n:
            return True
        return s[j] in [",", "}", "]"]

    while i < n:
        ch = s[i]

        if in_str:
            if esc:
                out.append(ch)
                esc = False
            else:
                if ch == "\\":
                    out.append(ch)
                    esc = True
                elif ch == '"':
                    if looks_like_string_end(i):
                        out.append(ch)
                        in_str = False
                    else:
                        out.append("'")
                else:
                    out.append(ch)
        else:
            if ch == '"':
                out.append(ch)
                in_str = True
                esc = False
            else:
                out.append(ch)

        i += 1

    return "".join(out)


def _try_parse_judge_array(judge_out) -> list[dict] | None:
    if not judge_out:
        return None

    if isinstance(judge_out, list):
        return judge_out

    if not isinstance(judge_out, str):
        return None

    s = _sanitize_judge_jsonish(judge_out)

    # 1) direct parse
    try:
        obj = json.loads(s)
        return obj if isinstance(obj, list) else None
    except Exception:
        pass

    # 2) fallback: extract first array
    candidate = _extract_first_json_array(s)
    if candidate:
        candidate = _sanitize_judge_jsonish(candidate)
        try:
            obj = json.loads(candidate)
            return obj if isinstance(obj, list) else None
        except Exception:
            # 3) repair unescaped quotes inside strings
            repaired = _repair_unescaped_quotes_in_json_strings(candidate)
            repaired = _sanitize_judge_jsonish(repaired)
            try:
                obj = json.loads(repaired)
                return obj if isinstance(obj, list) else None
            except Exception:
                return None

    # 3b) last resort: repair whole text
    repaired = _repair_unescaped_quotes_in_json_strings(s)
    repaired = _sanitize_judge_jsonish(repaired)
    try:
        obj = json.loads(repaired)
        return obj if isinstance(obj, list) else None
    except Exception:
        return None


def _try_parse_judge_object(judge_out) -> dict | None:
    """
    Single-testcase counterpart to _try_parse_judge_array.

    Accepts a JSON object, or an array whose first element is the object, so
    that a judge assistant still emitting the array schema does not silently
    produce a record without scores.
    """
    def _coerce(obj):
        if isinstance(obj, dict):
            return obj
        if isinstance(obj, list) and obj and isinstance(obj[0], dict):
            return obj[0]
        return None

    if judge_out is None:
        return None
    if isinstance(judge_out, (dict, list)):
        return _coerce(judge_out)
    if not isinstance(judge_out, str):
        return None

    s = _sanitize_judge_jsonish(judge_out)

    # 1) direct parse
    try:
        return _coerce(json.loads(s))
    except Exception:
        pass

    # 2) array path (judge may still wrap the single evaluation in a list)
    arr = _try_parse_judge_array(s)
    if arr:
        return _coerce(arr)

    # 3) extract first object, repair if needed
    candidate = _extract_first_json_object(s)
    if candidate:
        candidate = _sanitize_judge_jsonish(candidate)
        try:
            return _coerce(json.loads(candidate))
        except Exception:
            repaired = _sanitize_judge_jsonish(
                _repair_unescaped_quotes_in_json_strings(candidate)
            )
            try:
                return _coerce(json.loads(repaired))
            except Exception:
                return None

    # 4) last resort: repair whole text
    repaired = _sanitize_judge_jsonish(_repair_unescaped_quotes_in_json_strings(s))
    try:
        return _coerce(json.loads(repaired))
    except Exception:
        return None


def _score_block_to_expected_schema(block: dict) -> dict:
    if not isinstance(block, dict):
        return {
            "scores": {"R": 1, "H": 1, "S": 1, "D": 1, "K": 1},
            "flags": {
                "safety_first": False,
                "escalation_present": False,
                "offline_workflow_mentioned": False,
                "hallucination_suspected": False,
            },
            "missing_elements": ["judge_output_not_dict"],
            "short_justification": "",
        }

    scores = block.get("scores") if isinstance(block.get("scores"), dict) else {}
    flags = block.get("flags") if isinstance(block.get("flags"), dict) else {}

    def _clamp_1_5(x, default=1):
        try:
            v = int(x)
            return max(1, min(5, v))
        except Exception:
            return default

    block["scores"] = {
        "R": _clamp_1_5(scores.get("R", 1)),
        "H": _clamp_1_5(scores.get("H", 1)),
        "S": _clamp_1_5(scores.get("S", 1)),
        "D": _clamp_1_5(scores.get("D", 1)),
        "K": _clamp_1_5(scores.get("K", 1)),
    }

    block["flags"] = {
        "safety_first": bool(flags.get("safety_first", False)),
        "escalation_present": bool(flags.get("escalation_present", False)),
        "offline_workflow_mentioned": bool(flags.get("offline_workflow_mentioned", False)),
        "hallucination_suspected": bool(flags.get("hallucination_suspected", False)),
    }

    me = block.get("missing_elements")
    block["missing_elements"] = me if isinstance(me, list) else []

    sj = block.get("short_justification")
    block["short_justification"] = sj if isinstance(sj, str) else ""

    return block


def _norm_test_id(s: str) -> str:
    return (s or "").strip()


# ----------------------------
# Judge prompts
# ----------------------------
def _build_judge_prompt_single(tc: dict, assistant_answer: str, expected_elements: str, judge_context: dict | None = None) -> str:
    user_message = tc["input"]["prompt"]
    # judge_context is supplied by the caller for every strategy: the model-facing
    # context for S0/S1/S2, the original four-dimensional context for the two
    # unstructured variants whose model-facing context is a derived string.
    context_json = judge_context if judge_context is not None else (tc["input"].get("context") or {})
    meta = tc["input"].get("meta") or {}
    asset_type = meta.get("asset_type", "unknown")
    fault_type = meta.get("fault_type", "unknown")

    return f"""TESTCASE (User message):
<<<
{user_message}
>>>

CONTEXT (JSON):
<<<
{_safe_json_dumps(context_json)}
>>>

MODEL ANSWER:
<<<
{assistant_answer}
>>>

RUBRIC:
• R Relevanz (1-5)
• H Handlungsfähigkeit/Struktur (1-5)
• S Sicherheit/Eskalation (1-5)
• D Dokumentation/Nachvollziehbarkeit (1-5)
• K Kontextnutzung/Robustheit (1-5)

EXPECTED ELEMENTS (Fault-Type: {fault_type}, Domain: {asset_type}):
<<<
{expected_elements}
>>>

Bitte gib nur JSON im definierten Schema zurück.
WICHTIG: Gib gültiges JSON aus. In String-Feldern (z.B. short_justification) benutze keine doppelten Anführungszeichen ".
Wenn nötig, ersetze sie durch einfache Anführungszeichen ' oder escape als \\\".
"""


def _build_judge_prompt_incident(
    incident_id: str,
    generated_answers: list[dict],
    expected_elements: str,
    asset_type: str,
    fault_type: str,
) -> str:
    blocks = []
    for row in generated_answers:
        row_strategy = row.get("strategy", "")
        if row_strategy in ("S0_RAW", "S0_UNSTRUCTURED"):
            judge_ctx = row.get("original_context") or row.get("context_json") or {}
        else:
            judge_ctx = row.get("context_json") or {}
        blocks.append(
            f"""
--- {row["test_id"]} ({row.get("context_level","")}) ---
USER_MESSAGE:
{row["user_message"]}

CONTEXT_JSON:
{_safe_json_dumps(judge_ctx)}

ANSWER:
{row["answer"]}
"""
        )

    return f"""Du bekommst mehrere Antworten zum selben Incident, jeweils mit unterschiedlicher Kontextstrategie (S0, S0_RAW, S0_UNSTRUCTURED, S1, S2).

Bewerte JEDEN Block separat nach derselben Rubrik.
Gib ausschließlich ein gültiges JSON-Array zurück (eine Bewertung pro Block) im Schema:

[
  {{
    "test_id": "...",
    "scores": {{"R":1,"H":1,"S":1,"D":1,"K":1}},
    "flags": {{
      "safety_first": false,
      "escalation_present": false,
      "offline_workflow_mentioned": false,
      "hallucination_suspected": false
    }},
    "missing_elements": [],
    "short_justification": ""
  }}
]

INCIDENT_ID: {incident_id}
DOMAIN(asset_type): {asset_type}
FAULT_TYPE: {fault_type}

EXPECTED ELEMENTS:
<<<
{expected_elements}
>>>

WICHTIG: Gib gültiges JSON aus. In String-Feldern (z.B. short_justification) benutze keine doppelten Anführungszeichen ".
Wenn nötig, ersetze sie durch einfache Anführungszeichen ' oder escape als \\\".

BLOCKS:
{''.join(blocks)}
"""


# ----------------------------
# Strategy helpers
# ----------------------------
def _strategy_of(tc: dict) -> str:
    meta = (tc.get("input") or {}).get("meta") or {}
    return str(meta.get("strategy") or "").strip().upper()


def _s2_meta_to_request_params(selection_meta: dict | None) -> dict:
    if not isinstance(selection_meta, dict):
        return {
            "s2_selector_version": None,
            "s2_guardrails_version": None,
            "s2_trigger_signals": None,
            "s2_budget_chars": None,
            "s2_used_chars": None,
            "s2_selected_fields": None,
            "s2_dropped_fields": None,
            "s2_compressed_fields": None,
        }

    bp = selection_meta.get("budget_policy") or {}
    return {
        "s2_selector_version": selection_meta.get("selector_version"),
        "s2_guardrails_version": selection_meta.get("guardrails_version"),
        # B2: triggers are no longer visible in the transmitted context, so
        # they must be persisted here to keep each S2 record self-describing.
        "s2_trigger_signals": selection_meta.get("trigger_signals"),
        "s2_budget_chars": bp.get("max"),
        "s2_used_chars": bp.get("used"),
        "s2_selected_fields": selection_meta.get("selected_fields"),
        "s2_dropped_fields": selection_meta.get("dropped_fields"),
        "s2_compressed_fields": selection_meta.get("compressed_fields"),
    }


def _apply_s2_if_strategy(tc: dict, context: dict) -> tuple[dict, dict | None]:
    """
    S2 Hook (deterministic):
    - If meta.strategy == 'S2' AND meta.context_level == 'L2_full'
      => build L2B, inject context=selected subset, keep audit in _selection_meta
    Returns (context_for_model, selection_meta_or_none).
    """
    input_data = tc.get("input") or {}
    meta = input_data.get("meta") or {}

    strategy = str(meta.get("strategy") or "").strip().upper()
    context_level = str(meta.get("context_level") or "").strip()

    is_s2_variant = strategy == "S2" or strategy.startswith("S2_ABL_")
    if not (is_s2_variant and context_level == "L2_full"):
        return context or {}, None

    budget_chars = int(os.getenv("S2_BUDGET_CHARS", "3500"))

    # Domain dispatch: signal assets have traffic_signals/button_operated keys.
    # Operates on the context as loaded, before normalize_l2() prunes null leaves.
    ctx_asset = (context or {}).get("asset") or {}
    is_signal_domain = "traffic_signals" in ctx_asset or "button_operated" in ctx_asset
    if is_signal_domain:
        s2_out = s2_signal.build_l2b(context or {}, budget=s2_signal.BudgetPolicy(max_chars=budget_chars))
    else:
        s2_out = s2.build_l2b(context or {}, budget=s2.BudgetPolicy(max_chars=budget_chars))

    ctx_selected = s2_out.get("context") or {}
    selection_meta = s2_out.get("selection_meta") or {}

    # B2: the selection metadata is an audit artefact and is NOT transmitted
    # to the model. It is persisted via _s2_meta_to_request_params().
    return ctx_selected, selection_meta


# ----------------------------
# Unstructured context helpers
# ----------------------------
def _resolve_prompt_and_context(prompt: str, context: dict, strategy: str) -> tuple[str, dict | None]:
    """
    For S0_raw and S0_unstructured, the context_json contains a pre-formatted
    text string. Extract it and append directly to the prompt so the client
    does not need modification.
    Returns (final_prompt, context_for_client).
    """
    if strategy == "S0_RAW":
        text = (context or {}).get("_raw_text", "")
        if text:
            return prompt + " " + text, None
    if strategy == "S0_UNSTRUCTURED":
        text = (context or {}).get("_unstructured_text", "")
        if text:
            return prompt + " " + text, None
    return prompt, context


def run_testcase(tc: dict, enable_judge: bool | None = None):
    """
    Single-testcase mode: one generation, one judge call, one log record.

    Each response is judged in isolation, without the other strategy variants
    of the same incident being present in the judge prompt.
    """
    enable_judge = ENABLE_JUDGE_DEFAULT if enable_judge is None else enable_judge

    test_id = tc["test_id"]
    client_name = _normalize_client_name(tc.get("client", "506"))

    model = tc.get("model") or os.getenv("TESTSUITE_DEFAULT_MODEL", "gpt-4.1")

    input_data = tc["input"]
    input_type = input_data.get("type", "text")
    prompt = input_data.get("prompt")
    context = input_data.get("context") or {}
    image_path = input_data.get("image_path")
    audio_path = input_data.get("audio_path")
    video_path = input_data.get("video_path")

    strategy = _strategy_of(tc)
    suite_version = tc.get("suite_version", "v0.2")

    # Original L2_full context, kept for judge reference BEFORE any transformation
    original_context = dict(context) if context else {}

    # ---- S2 hook ----
    context_for_model, selection_meta = _apply_s2_if_strategy(tc, context)

    # ---- unstructured context hook ----
    prompt, context_for_model = _resolve_prompt_and_context(prompt, context_for_model, strategy)

    if client_name not in CLIENTS:
        raise ValueError(f"Unbekannter Client: '{client_name}'")
    client = CLIENTS[client_name]

    result_dir = _result_dir_for_client(client_name, model)

    # Reconstruct the prompt as the client composes it, so the log holds the
    # string actually sent to the model (including the [CONTEXT_JSON] block).
    final_prompt = _final_prompt_for_log(client, prompt, context_for_model)

    has_judge = enable_judge and hasattr(client, "judge")
    judge_model = os.getenv("TESTSUITE_JUDGE_MODEL", model)
    judge_temp = float(os.getenv("TESTSUITE_JUDGE_TEMPERATURE", "0.0"))
    judge_mode = os.getenv("TESTSUITE_JUDGE_MODE", "BASIC")
    judge_version = os.getenv("TESTSUITE_JUDGE_VERSION", "judge_v1_0")

    media_block = {
        "image_path": image_path,
        "audio_path": audio_path,
        "video_path": video_path,
    }

    start = time.perf_counter()
    answer = client.generate(
        input_type=input_type,
        prompt=prompt,
        model=model,
        context=context_for_model,
        image_path=image_path,
        audio_path=audio_path,
        video_path=video_path,
    )
    runtime = round(time.perf_counter() - start, 3)

    # ---- generation failure: log as error, do not judge ----
    if _is_client_error_answer(answer):
        print(f"[ERROR] {test_id}: generation failed -> {str(answer)[:200]}")
        log_response(
            test_id=test_id,
            prompt=final_prompt,
            response_text=answer,
            model=model,
            client=client_name,
            runtime_seconds=runtime,
            input_type=input_type,
            result_dir=result_dir,
            run_index=None,
            suite_version=suite_version,
            request_params={
                "run_mode": "testcase",
                "assistant_source_of_truth": True,
                "context_strategy": strategy or "UNKNOWN",
                "user_message": input_data.get("prompt"),
                "judge_version": None,
                "judge_model": None,
                "judge_temperature": None,
                "judge_mode": None,
                **_s2_meta_to_request_params(None),
            },
            judge=None,
            input_context=context_for_model,
            media=media_block,
            error={"stage": "generate", "message": str(answer)},
        )
        return

    # ---- judging ----
    judge_out = None
    if has_judge:
        expected_elements = (input_data.get("meta") or {}).get("expected_elements_short", "")

        # Mirror the incident-group mode: the judge sees the context the model
        # received, except for the two unstructured variants, whose model-facing
        # context is a derived string rather than the structured object.
        if strategy in ("S0_RAW", "S0_UNSTRUCTURED"):
            judge_context = original_context
        else:
            judge_context = context_for_model or {}

        judge_prompt = _build_judge_prompt_single(
            tc, answer, expected_elements, judge_context=judge_context
        )
        judge_raw = client.judge(
            prompt=judge_prompt,
            model=judge_model,
            temperature=judge_temp,
            selected_mode=judge_mode,
            internal_system_prompt=False,
        )

        # Raw judge artefact per test case, mirroring the per-incident artefact
        # of group mode, so that the repair procedure stays auditable.
        artifact_dir = os.path.join(result_dir, test_id)
        os.makedirs(artifact_dir, exist_ok=True)
        artifact_path = os.path.join(artifact_dir, "judge_raw.json")
        with open(artifact_path, "w", encoding="utf-8") as f:
            f.write(
                judge_raw if isinstance(judge_raw, str)
                else json.dumps(judge_raw, ensure_ascii=False, indent=2)
            )

        if _is_client_error_answer(judge_raw):
            print(f"[ERROR] {test_id}: judge call failed -> {str(judge_raw)[:200]}")
            judge_out = _score_block_to_expected_schema(
                {
                    "test_id": test_id,
                    "missing_elements": ["judge_call_failed"],
                    "short_justification": "Judge-Aufruf fehlgeschlagen; Fallback gesetzt.",
                }
            )
        else:
            parsed = _try_parse_judge_object(judge_raw)
            if parsed is None:
                print(f"[WARN] {test_id}: judge output could not be parsed (after repair).")
                judge_out = _score_block_to_expected_schema(
                    {
                        "test_id": test_id,
                        "missing_elements": ["judge_parse_failed"],
                        "short_justification": "Judge-Ausgabe nicht parsebar; Fallback gesetzt.",
                    }
                )
            else:
                parsed.setdefault("test_id", test_id)
                judge_out = _score_block_to_expected_schema(parsed)

    # Ablation variants also pass through the policy, so their audit trail
    # must be persisted as well.
    is_s2_variant = strategy == "S2" or strategy.startswith("S2_ABL_")
    s2_params = _s2_meta_to_request_params(selection_meta if is_s2_variant else None)

    log_response(
        test_id=test_id,
        prompt=final_prompt,
        response_text=answer,
        model=model,
        client=client_name,
        runtime_seconds=runtime,
        input_type=input_type,
        result_dir=result_dir,
        run_index=None,
        suite_version=suite_version,
        request_params={
            "run_mode": "testcase",
            "incident_id": (input_data.get("meta") or {}).get("incident_id", "UNKNOWN"),
            "assistant_source_of_truth": True,
            "context_strategy": strategy or "UNKNOWN",
            # Kept separate from `prompt`, which now carries the composed form.
            "user_message": input_data.get("prompt"),
            "judge_version": judge_version if has_judge else None,
            "judge_model": judge_model if has_judge else None,
            "judge_temperature": judge_temp if has_judge else None,
            "judge_mode": judge_mode if has_judge else None,
            **s2_params,
        },
        judge=judge_out,
        input_context=context_for_model,
        media=media_block,
        error=None,
    )


def run_incident_group(testcases: list[dict], enable_judge: bool | None = None):
    """
    Incident-group mode: all strategy variants of one incident are generated
    first and judged together in a single judge request.
    """
    enable_judge = ENABLE_JUDGE_DEFAULT if enable_judge is None else enable_judge
    if not testcases:
        return

    _strategy_order = {"S0": 1, "S0_RAW": 2, "S0_UNSTRUCTURED": 3, "S1": 4, "S2": 5}
    testcases = sorted(testcases, key=lambda x: _strategy_order.get(
        str(((x.get("input") or {}).get("meta") or {}).get("strategy") or "").strip().upper(), 99
    ))

    client_name = _normalize_client_name(testcases[0].get("client", "506"))
    if client_name not in CLIENTS:
        raise ValueError(f"Unbekannter Client: '{client_name}'")
    client = CLIENTS[client_name]

    default_model = testcases[0].get("model") or os.getenv("TESTSUITE_DEFAULT_MODEL", "gpt-4.1")

    has_judge = enable_judge and hasattr(client, "judge")
    judge_model = os.getenv("TESTSUITE_JUDGE_MODEL", default_model)
    judge_temp = float(os.getenv("TESTSUITE_JUDGE_TEMPERATURE", "0.0"))
    judge_mode = os.getenv("TESTSUITE_JUDGE_MODE", "BASIC")
    judge_version = os.getenv("TESTSUITE_JUDGE_VERSION", "judge_v1_0")

    meta0 = testcases[0].get("input", {}).get("meta") or {}
    incident_id = meta0.get("incident_id", "UNKNOWN")
    asset_type = meta0.get("asset_type", "unknown")
    fault_type = meta0.get("fault_type", "unknown")
    expected_elements = meta0.get("expected_elements_short", "")

    out_dir = _result_dir_for_client(client_name, default_model)
    os.makedirs(out_dir, exist_ok=True)

    generated: list[dict] = []
    runtimes: dict[str, float] = {}

    for tc in testcases:
        input_data = tc["input"]
        test_id = tc["test_id"]

        model = tc.get("model") or default_model

        strategy = _strategy_of(tc)

        base_context = input_data.get("context") or {}
        original_context_inc = dict(base_context) if base_context else {}
        context_for_model, selection_meta = _apply_s2_if_strategy(tc, base_context)
        inc_prompt, context_for_model = _resolve_prompt_and_context(
            input_data.get("prompt"), context_for_model, strategy
        )

        # Composed form, captured before dispatch so the log can hold it.
        final_prompt = _final_prompt_for_log(client, inc_prompt, context_for_model)

        start = time.perf_counter()
        ans = client.generate(
            input_type=input_data.get("type", "text"),
            prompt=inc_prompt,
            model=model,
            context=context_for_model,
            image_path=input_data.get("image_path"),
            audio_path=input_data.get("audio_path"),
            video_path=input_data.get("video_path"),
        )
        runtimes[test_id] = round(time.perf_counter() - start, 3)

        if _is_client_error_answer(ans):
            print(f"[ERROR] {test_id}: generation failed -> {str(ans)[:200]}")

        generated.append(
            {
                "test_id": test_id,
                "context_level": (input_data.get("meta") or {}).get("context_level", ""),
                "user_message": input_data.get("prompt"),
                "final_prompt": final_prompt,
                "context_json": context_for_model or {},
                "original_context": original_context_inc,
                "answer": ans,
                "model": model,
                "selection_meta": selection_meta,
                "strategy": strategy,
                "generation_failed": _is_client_error_answer(ans),
            }
        )

    judge_array: list[dict] | None = None
    judge_raw_clean: str | None = None
    judge_raw_any = None

    if has_judge:
        judge_prompt = _build_judge_prompt_incident(
            incident_id=incident_id,
            generated_answers=generated,
            expected_elements=expected_elements,
            asset_type=asset_type,
            fault_type=fault_type,
        )

        judge_raw_any = client.judge(
            prompt=judge_prompt,
            model=judge_model,
            temperature=judge_temp,
            selected_mode=judge_mode,
            internal_system_prompt=False,
        )

        judge_raw_str = (
            judge_raw_any
            if isinstance(judge_raw_any, str)
            else json.dumps(judge_raw_any, ensure_ascii=False, indent=2)
        )
        judge_raw_clean = _sanitize_judge_jsonish(judge_raw_str)

        artifact_path = os.path.join(out_dir, f"{incident_id}__judge.json")
        with open(artifact_path, "w", encoding="utf-8") as f:
            f.write(judge_raw_clean)
        print(f"[LOG] Judge-Artifact gespeichert unter: {artifact_path}")

        judge_array = _try_parse_judge_array(judge_raw_clean)

        if judge_raw_clean and not judge_array:
            print("[WARN] Judge-Artifact gespeichert, aber JSON-Array konnte nicht geparsed werden (nach Repair).")

    # Build mapping
    judge_by_test_id: dict[str, dict] = {}

    # 1) primary mapping by test_id
    if judge_array:
        for block in judge_array:
            if isinstance(block, dict) and block.get("test_id"):
                judge_by_test_id[_norm_test_id(block["test_id"])] = _score_block_to_expected_schema(block)

    # 2) fallback: if count matches, map by position
    if judge_array and len(judge_array) == len(generated):
        for i, row in enumerate(generated):
            tid = _norm_test_id(row.get("test_id"))
            if tid and tid not in judge_by_test_id:
                b = judge_array[i]
                if isinstance(b, dict):
                    b2 = dict(b)
                    b2["test_id"] = row.get("test_id")
                    judge_by_test_id[tid] = _score_block_to_expected_schema(b2)

    # 3) mismatch warning
    if judge_array and len(judge_array) != len(generated):
        print(f"[WARN] Judge blocks count mismatch: judge={len(judge_array)} vs generated={len(generated)}")

    # Attach per-test logs
    for row in generated:
        test_id = row["test_id"]
        tc = next(t for t in testcases if t["test_id"] == test_id)
        input_data = tc["input"]
        model = row.get("model") or default_model

        strategy = row.get("strategy") or _strategy_of(tc)
        selection_meta = row.get("selection_meta") or None

        judge_block = judge_by_test_id.get(_norm_test_id(test_id)) if judge_by_test_id else None
        if has_judge and judge_raw_clean and not judge_block:
            judge_block = _score_block_to_expected_schema(
                {
                    "test_id": test_id,
                    "missing_elements": ["judge_block_missing_fallback"],
                    "short_justification": "Judge-Array enthielt keinen Block für diese Antwort; Fallback gesetzt.",
                }
            )

        is_s2_variant = strategy == "S2" or strategy.startswith("S2_ABL_")
        s2_params = _s2_meta_to_request_params(selection_meta if is_s2_variant else None)

        gen_failed = bool(row.get("generation_failed"))

        log_response(
            test_id=test_id,
            prompt=row.get("final_prompt") or input_data.get("prompt"),
            response_text=row["answer"],
            model=model,
            client=client_name,
            runtime_seconds=runtimes.get(test_id, -1),
            input_type=input_data.get("type", "text"),
            result_dir=out_dir,
            run_index=None,
            suite_version=tc.get("suite_version", "v0.2"),
            request_params={
                "run_mode": "incident",
                "incident_id": incident_id,
                "assistant_source_of_truth": True,
                "context_strategy": strategy or "UNKNOWN",
                # Kept separate from `prompt`, which now carries the composed form.
                "user_message": input_data.get("prompt"),
                "judge_version": judge_version if has_judge else None,
                "judge_model": judge_model if has_judge else None,
                "judge_temperature": judge_temp if has_judge else None,
                "judge_mode": judge_mode if has_judge else None,
                **s2_params,
            },
            judge=judge_block,
            input_context=row.get("context_json") or {},
            media={
                "image_path": input_data.get("image_path"),
                "audio_path": input_data.get("audio_path"),
                "video_path": input_data.get("video_path"),
            },
            error={"stage": "generate", "message": str(row["answer"])} if gen_failed else None,
        )

    if has_judge and judge_raw_clean and not judge_array:
        print(
            "[WARN] Judge-Output konnte nicht als JSON-Array geparsed werden. "
            "Raw-Artifact ist gespeichert, aber per-testcase Judge-Blocks wurden nicht attached."
        )