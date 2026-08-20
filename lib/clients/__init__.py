# lib/clients/__init__.py

from lib.clients import companygpt_client

CLIENTS = {
    "506": companygpt_client,
    "companygpt": companygpt_client
}