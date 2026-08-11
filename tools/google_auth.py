"""Shared OAuth credential loading for Sheets/Docs/YouTube-upload tools.

All tools that need Google OAuth (as opposed to the read-only YouTube API
key) import get_credentials() from here instead of each carrying their own
copy of the consent flow.

Run with: .venv/bin/python -u tools/some_tool.py ...
(the -u matters if the flow needs to print the consent URL to a redirected
log before it can be read)
"""

import os

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(ROOT, "credentials.json")
TOKEN_PATH = os.path.join(ROOT, "token.json")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/youtube.upload",
]


def get_credentials():
    load_dotenv(os.path.join(ROOT, ".env"))
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_PATH):
                raise SystemExit(f"FAIL: {CREDENTIALS_PATH} not found")
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            print("Open this URL in your browser to grant access:", flush=True)
            creds = flow.run_local_server(port=0, open_browser=False)
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
    return creds
