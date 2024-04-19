from utils.setup_driver import setup_driver
from utils.get_value_from_sheets import get_value_from_sheets
from automation.reservation import reservation_automation
from automation.analyze import analyze_automation
from utils.generate_date_ranges import generate_date_ranges
import os

URL1 = os.environ.get("URL1")
URL2 = os.environ.get("URL2")
COMPANY_CODE = os.environ.get("COMPANY_CODE")
FACILITY_NAME = os.environ.get("FACILITY_NAME")

def reservation_entry(event, context):
    print("Start : reservation")
    date_ranges = [];
    date_ranges = generate_date_ranges()
    date_len = len(date_ranges)
    file_names = [f"{FACILITY_NAME}_{i:02d}.CSV" for i in range(1, date_len + 1)]
    value1, value2 = get_value_from_sheets()
    driver = setup_driver()
    reservation_automation(driver, value1, value2, URL1, URL2, COMPANY_CODE, date_ranges, file_names)
    print("Finished : reservation")
    driver.close()
    driver.quit()

def analyze_entry(event, context):
    print("Start")
    date_ranges = [];
    date_ranges = generate_date_ranges()
    date_len = len(date_ranges)
    file_names = [f"{FACILITY_NAME}_analyze_{i:02d}.CSV" for i in range(1, date_len + 1)]
    value1, value2 = get_value_from_sheets()
    driver = setup_driver()
    analyze_automation(driver, value1, value2, URL1, URL2, COMPANY_CODE, date_ranges, file_names)
    print("Finished")
    driver.close()
    driver.quit()
