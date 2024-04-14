from utils.setup_driver import setup_driver
from utils.get_value_from_sheets import get_value_from_sheets
from automation.automation_part import automation_part
from utils.generate_date_ranges import generate_date_ranges
import os

URL1 = os.environ.get("URL1")
URL2 = os.environ.get("URL2")
COMPANY_CODE = os.environ.get("COMPANY_CODE")
FACILITY_NAME = os.environ.get("FACILITY_NAME") # automate this part later
# FILE_NAMES = [ # automate this part later
#     'facilname_01.CSV',
#     'facilname_02.CSV',
#     'facilname_03.CSV',
#     'facilname_04.CSV',
#     'facilname_05.CSV',
#     'facilname_06.CSV',
#     'facilname_07.CSV',
#     'facilname_08.CSV',
#     'facilname_09.CSV',
#     'facilname_10.CSV',
#     'facilname_11.CSV',
#     'facilname_12.CSV',
#     'facilname_13.CSV',
#     'facilname_14.CSV',
#     'facilname_15.CSV',
#     'facilname_16.CSV',
#     'facilname_17.CSV',
#     'facilname_18.CSV',
#     'facilname_19.CSV',
#     'facilname_20.CSV',
#     'facilname_21.CSV',
#     'facilname_22.CSV',
#     'facilname_23.CSV',
#     'facilname_24.CSV'
# ]

def main(event, context):
    date_ranges = [];
    date_ranges = generate_date_ranges()
    date_len = len(date_ranges)
    file_names = [f"{FACILITY_NAME}_{i:02d}.CSV" for i in range(1, date_len + 1)]
    value1, value2 = get_value_from_sheets()
    driver = setup_driver()
    automation_part(driver, value1, value2, URL1, URL2, COMPANY_CODE, date_ranges, file_names)
    print("Finished")
    driver.close()
    driver.quit()
