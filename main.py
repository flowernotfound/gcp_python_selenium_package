from utils.setup_driver import setup_driver
from utils.get_value_from_sheets import get_value_from_sheets
# for reservation
# from automation.reservation import automation_part
# for analyze
from automation.analyze import automation_part
from utils.generate_date_ranges import generate_date_ranges
import os

URL1 = os.environ.get("URL1")
URL2 = os.environ.get("URL2")
COMPANY_CODE = os.environ.get("COMPANY_CODE")
FACILITY_NAME = os.environ.get("FACILITY_NAME")

def main(event, context):
    print("Start")
    date_ranges = [];
    date_ranges = generate_date_ranges()
    date_len = len(date_ranges)
    # for reservation
    # file_names = [f"{FACILITY_NAME}_{i:02d}.CSV" for i in range(1, date_len + 1)]
    # for analyze
    file_names = [f"{FACILITY_NAME}_analyze_{i:02d}.CSV" for i in range(1, date_len + 1)]
    value1, value2 = get_value_from_sheets()
    driver = setup_driver()
    automation_part(driver, value1, value2, URL1, URL2, COMPANY_CODE, date_ranges, file_names)
    print("Finished")
    driver.close()
    driver.quit()
