from datetime import datetime, timedelta

def format_date(date_obj: datetime) -> str:
    """Format a datetime object to 'YYYY-MM-DD' string."""
    return date_obj.strftime('%Y-%m-%d')

def is_valid_date(date_str: str) -> bool:
    """Check if a string is a valid date in 'YYYY-MM-DD' format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_week_range(date_str: str) -> tuple[str, str]:
    """Return start and end date (YYYY-MM-DD) of the week for a given date."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    start = date_obj - timedelta(days=date_obj.weekday())
    end = start + timedelta(days=6)
    return format_date(start), format_date(end)
