import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from time import sleep
from setup_driver import setup_driver
from get_credentials import get_credentials
from get_value_from_sheets import get_login_details

TOP_URL = os.environ.get("TOP_URL")
RESERVATION_URL = os.environ.get("RESERVATION_URL")
COMPANY_CODE = os.environ.get("COMPANY_CODE")
TARGET_FOLDER = os.environ.get("TARGET_FOLDER_ID")
DATE_RANGES = [
    ['2024/04/01', '2024/04/20']
]
FILE_NAMES = [
    '泊屋上野_01_20240401_20240420.CSV'
]

def upload_file_to_drive(file_name):
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': file_name,
        'parents': [TARGET_FOLDER]
    }
    media = MediaFileUpload(f'/tmp/{file_name}', mimetype='text/csv')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Uploaded {file_name} to Google Drive with ID: {file.get('id')}")

def select_month(driver, from_date, to_date):
    driver.find_element(By.ID, 'searchStayStartDate').send_keys(from_date)
    driver.find_element(By.ID, 'searchStayEndDate').send_keys(to_date)

def download_csv_for_date_range(driver, date_range, file_name):
    select_month(driver, date_range[0], date_range[1])
    driver.find_element(By.ID, 'doSearch').click()
    sleep(3)
    driver.find_element(By.ID, 'CsvOut').click()
    sleep(4)
    downloaded_files = os.listdir('/tmp')
    csv_files = [file for file in downloaded_files if file.endswith('.CSV')]
    
    if len(csv_files) > 0:
        latest_csv = max(csv_files, key=lambda f: os.path.getctime(os.path.join('/tmp', f)))
        old_path = os.path.join('/tmp', latest_csv)
        new_path = os.path.join('/tmp', file_name)
        os.rename(old_path, new_path)
        print(f"Renamed downloaded file from {latest_csv} to {file_name}")
    else:
        print("No CSV file found in the download directory")
    upload_file_to_drive(file_name)

def list_downloaded_files():
    files = os.listdir('/tmp')
    print("Downloaded files:")
    for file in files:
        file_path = os.path.join('/tmp', file)
        print(f"File: {file}, Size: {os.path.getsize(file_path)} bytes")

def exec_search(event, context):
    login_id, password = get_login_details()
    driver = setup_driver()
    
    try:
        driver.get(TOP_URL) #("https://www37.neppan.net/")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'clientCode').send_keys(COMPANY_CODE)
        driver.find_element(By.ID, 'loginId').send_keys(login_id)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.LINK_TEXT, 'ログイン').click()
        driver.get(RESERVATION_URL) #("https://www37.neppan.net/reservationView.php")
        driver.find_element(By.ID, 'hideButton').click()
        driver.find_element(By.CSS_SELECTOR, "label[for='searchStatusArg3']").click()
        
        for date_range, file_name in zip(DATE_RANGES, FILE_NAMES):
            print(f"Downloading CSV for date range: {date_range}")
            download_csv_for_date_range(driver, date_range, file_name)
        
        print("Listing downloaded files:")
        list_downloaded_files()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        driver.close()
        driver.quit()