from setup_driver import setup_driver
from get_value_from_sheets import get_value_from_sheets
from automation import automation_part
import os

URL1 = os.environ.get("TOP_URL")
URL2 = os.environ.get("RESERVATION_URL")
COMPANY_CODE = os.environ.get("COMPANY_CODE")
DATE_RANGES = [
    ['2024/04/01', '2024/04/20']
]
FILE_NAMES = [
    'test_01_20240401_20240420.CSV'
]

def main(event, context):
    value1, value2 = get_value_from_sheets()
    driver = setup_driver()
    automation_part(driver, value1, value2, URL1, URL2, COMPANY_CODE, DATE_RANGES, FILE_NAMES)
    driver.close()
    driver.quit()
