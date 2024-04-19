from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def generate_date_half_ranges():
    date_ranges = []
    current_year = datetime.now().year
    current_month = datetime.now().month

    for month_delta in range(12):
        month_start_date = datetime(current_year, current_month, 1) + relativedelta(months=month_delta)
        mid_month_date = month_start_date.replace(day=15)
        end_of_month_date = month_start_date + relativedelta(months=1) - timedelta(days=1)
        
        first_period_start = month_start_date.strftime('%Y/%m/%d')
        first_period_end = mid_month_date.strftime('%Y/%m/%d')
        second_period_start = (mid_month_date + timedelta(days=1)).strftime('%Y/%m/%d')
        second_period_end = end_of_month_date.strftime('%Y/%m/%d')
        
        date_ranges.append([first_period_start, first_period_end])
        date_ranges.append([second_period_start, second_period_end])
    
    return date_ranges

def generate_monthly_date_ranges():
    date_ranges = []
    current_year = datetime.now().year
    current_month = datetime.now().month

    for month_delta in range(12):
        month_start_date = datetime(current_year, current_month, 1) + relativedelta(months=month_delta)
        end_of_month_date = month_start_date + relativedelta(months=1) - timedelta(days=1)
        
        period_start = month_start_date.strftime('%Y/%m/%d')
        period_end = end_of_month_date.strftime('%Y/%m/%d')
        
        date_ranges.append([period_start, period_end])
    
    return date_ranges