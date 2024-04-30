from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from utils.upload_file_to_drive import upload_file_to_drive
import os
from utils.send_error_email import send_error_email

def select_analyze_month(driver, from_date, to_date):
    driver.find_element(By.ID, 'txtFromDate').send_keys(from_date)
    driver.find_element(By.ID, 'txtToDate').send_keys(to_date)

def download_csv(driver, date_range):
    select_analyze_month(driver, date_range[0], date_range[1])
    driver.find_element(By.ID, 'btnSearch').click()
    target_element = driver.find_element(By.ID, "btnReportCSV")
    driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
    sleep(1)
    target_element.click()
    driver.execute_script("window.scrollTo(0, 0);")
    sleep(5)

def clear_analyze_form(driver):
    driver.find_element(By.ID, 'txtFromDate').clear()
    driver.find_element(By.ID, 'txtToDate').clear()

def find_and_upload_csv(file_name):
    downloaded_files = os.listdir('/tmp')
    csv_files = [file for file in downloaded_files if file.endswith('.CSV')]
    
    if len(csv_files) > 0:
        latest_csv = max(csv_files, key=lambda f: os.path.getctime(os.path.join('/tmp', f)))
        old_path = os.path.join('/tmp', latest_csv)
        new_path = os.path.join('/tmp', file_name)
        os.rename(old_path, new_path)
    else:
        print("No CSV file found in the download directory")

def login(driver,COMPANY_CODE, login_id, password):
    driver.find_element(By.ID, 'clientCode').send_keys(COMPANY_CODE)
    driver.find_element(By.ID, 'loginId').send_keys(login_id)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.LINK_TEXT, 'ログイン').click()

def analyze_automation(driver, login_id, password, TOP_URL, ANALYZE_URL, COMPANY_CODE, DATE_RANGES, FILE_NAMES):
    try:
        driver.get(TOP_URL)
        driver.implicitly_wait(5)
        login(driver, COMPANY_CODE, login_id, password)
        driver.get(ANALYZE_URL)
        driver.find_element(By.ID, 'hideKensakuDispButton').click()
        select_style_element = driver.find_element(By.ID, "cmbOutputStyle")
        select_style_object = Select(select_style_element)
        select_style_object.select_by_value("2")
        select_element = driver.find_element(By.ID, "cmbSum")
        select_object = Select(select_element)
        select_object.select_by_value("1")
        
        for date_range, file_name in zip(DATE_RANGES, FILE_NAMES):
            print(f"Downloading CSV for {date_range[0]} to {date_range[1]}")
            clear_analyze_form(driver)
            download_csv(driver, date_range)
            find_and_upload_csv(file_name)
            upload_file_to_drive(file_name)
            
    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(f"Error : {str(e)}")
        send_error_email(error_message)
