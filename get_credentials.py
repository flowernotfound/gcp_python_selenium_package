from google.oauth2.credentials import Credentials
import os

CLIENT_ID = os.environ.get("GCP_CLIENT_ID")
CLIENT_SECRET = os.environ.get("GCP_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("GCP_REFRESH_TOKEN")

def get_credentials():
    return Credentials(None, refresh_token=REFRESH_TOKEN, token_uri="https://oauth2.googleapis.com/token", client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
