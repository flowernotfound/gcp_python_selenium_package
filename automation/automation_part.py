from selenium.webdriver.common.by import By
from time import sleep
from utils.upload_file_to_drive import upload_file_to_drive
import os

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
    else:
        print("No CSV file found in the download directory")
    
    upload_file_to_drive(file_name)

def automation_part(driver, login_id, password, TOP_URL, RESERVATION_URL, COMPANY_CODE, DATE_RANGES, FILE_NAMES):
    try:
        driver.get(TOP_URL)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'clientCode').send_keys(COMPANY_CODE)
        driver.find_element(By.ID, 'loginId').send_keys(login_id)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.LINK_TEXT, 'ログイン').click()
        driver.get(RESERVATION_URL)
        driver.find_element(By.ID, 'hideButton').click()
        driver.find_element(By.CSS_SELECTOR, "label[for='searchStatusArg3']").click()
        
        for date_range, file_name in zip(DATE_RANGES, FILE_NAMES):
            download_csv_for_date_range(driver, date_range, file_name)
    except Exception as e:
        print(f"Error : {str(e)}")
