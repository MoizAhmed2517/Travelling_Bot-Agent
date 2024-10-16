from datetime import datetime

def check_dates_availability(check_in, check_out):
    try:
        # Convert the input strings to datetime objects
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")

        
    except ValueError:
        # If the input strings are not in the correct format, return False
        return False