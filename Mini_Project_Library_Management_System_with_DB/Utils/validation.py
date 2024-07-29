import re

def validate_isbn(isbn):
    if not re.match(r'^\d{10}(\d{3})?$', isbn):
        raise ValueError("Invalid ISBN format.")
    return True

def validate_user_id(user_id):
    if not re.match(r'^U\d{3}$', user_id):
        raise ValueError("Invalid user ID format.")
    return True

def validate_name(name):
    if not re.match(r'^[a-zA-Z\s]+$', name):
        raise ValueError("Invalid name format.")
    return True

def validate_date(date):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    return True
