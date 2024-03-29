from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from get_credentials import get_credentials
import os

TARGET_FOLDER = os.environ.get("TARGET_FOLDER_ID")

def upload_file_to_drive(file_name):
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': file_name,
        'parents': [TARGET_FOLDER]
    }
    media = MediaFileUpload(f'/tmp/{file_name}', mimetype='text/csv')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
