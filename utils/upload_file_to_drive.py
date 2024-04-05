from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from utils.get_credentials import get_credentials
import os

TARGET_FOLDER = os.environ.get("TARGET_FOLDER_ID")

def delete_existing_file(service, file_name, folder_id):
    query = f"name = '{file_name}' and '{folder_id}' in parents and trashed = false"
    response = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    for file in response.get('files', []):
        print(f"Deleting file: {file.get('name')} (ID: {file.get('id')})")
        service.files().delete(fileId=file.get('id')).execute()

def upload_file_to_drive(file_name):
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    delete_existing_file(service, file_name, TARGET_FOLDER)

    file_metadata = {
        'name': file_name,
        'parents': [TARGET_FOLDER]
    }
    
    media = MediaFileUpload(f'/tmp/{file_name}', mimetype='text/csv')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'Uploaded file ID: {file.get("id")}')
