from googleapiclient.discovery import build
from get_credentials import get_credentials
import os

SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
TAB_NAME = os.environ.get("TAB_NAME")
CELL_RANGE_LOGIN_ID = os.environ.get("CELL_RANGE_LOGIN_ID")
CELL_RANGE_PASSWORD = os.environ.get("CELL_RANGE_PASSWORD")

def get_login_details():
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    login_id_result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{TAB_NAME}!{CELL_RANGE_LOGIN_ID}").execute()
    password_result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{TAB_NAME}!{CELL_RANGE_PASSWORD}").execute()
    login_id = login_id_result.get('values', [['']])[0][0]
    password = password_result.get('values', [['']])[0][0]
    return login_id, password
