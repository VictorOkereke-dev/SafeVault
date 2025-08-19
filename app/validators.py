import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def is_strong_password(password):
    return len(password) >= 8 and any(char.isdigit() for char in password)
  
