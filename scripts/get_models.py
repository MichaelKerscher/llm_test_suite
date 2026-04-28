import os, requests
from dotenv import load_dotenv
load_dotenv()

r = requests.get(
    "https://plattform.506.ai:3003/api/v1/public/models",
    headers={
        "api-organization-id": os.getenv("COMPANYGPT_ORG_ID"),
        "api-key": os.getenv("COMPANYGPT_API_KEY"),
    }
)
print(r.json())