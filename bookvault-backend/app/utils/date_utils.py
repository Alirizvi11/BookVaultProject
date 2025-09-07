from datetime import datetime

def format_date(date_obj):
    return date_obj.strftime('%Y-%m-%d')

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_week_range(date_str):
    """Returns start and end date of the week for given date"""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    start = date_obj - timedelta(days=date_obj.weekday())
    end = start + timedelta(days=6)
    return format_date(start), format_date(end)
