from datetime import date, timedelta

def generate_date_range(start_date, end_date):
   
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)