from googleapiclient.discovery import build
from utils.get_credentials import get_credentials
import os

SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
TAB_NAME = os.environ.get("TAB_NAME")
CELL_RANGE1 = os.environ.get("CELL_RANGE1")
CELL_RANGE2 = os.environ.get("CELL_RANGE2")

def get_value_from_sheets(): # get value from Google Sheets
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    value1_result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{TAB_NAME}!{CELL_RANGE1}").execute()
    value2_result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{TAB_NAME}!{CELL_RANGE2}").execute()
    value1 = value1_result.get('values', [['']])[0][0]
    value2 = value2_result.get('values', [['']])[0][0]
    return value1, value2
