import os
from typing import Optional

import httplib2
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_httplib2 import AuthorizedHttp
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource


# TODO: SSL verification is disabled.
# This must be enabled before production.
http = httplib2.Http(
    disable_ssl_certificate_validation=True
)


# Full read/write access to Google Calendar
SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]


# These are relative to the directory from which you run the application.
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


def get_calendar_credentials() -> Credentials:
    """
    Retrieve, refresh, or create Google OAuth2 credentials.
    """

    creds: Optional[Credentials] = None

    # 1. Load existing token
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES,
        )

    # 2. Refresh or create credentials
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            print("Access token expired. Refreshing token...")
            creds.refresh(Request())

        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(
                    f"'{CREDENTIALS_FILE}' not found. "
                    "Place credentials.json in the project root."
                )

            print(
                "No valid token found. "
                "Launching browser for Google OAuth..."
            )

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES,
            )

            creds = flow.run_local_server(
                port=0
            )

        # Save credentials
        with open(TOKEN_FILE, "w") as token_file:
            token_file.write(creds.to_json())

        print(f"Credentials saved to {TOKEN_FILE}")

    return creds


def get_calendar_service() -> Resource:
    """
    Create an authorized Google Calendar API v3 client.
    """

    creds = get_calendar_credentials()

    authed_http = AuthorizedHttp(
        creds,
        http=http,
    )

    return build(
        "calendar",
        "v3",
        http=authed_http,
    )