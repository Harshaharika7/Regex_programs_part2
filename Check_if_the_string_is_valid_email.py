import re

def is_valid_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    match = email_pattern.match(email)
    return bool(match)
email_to_check = input("Enter an email address: ")

if is_valid_email(email_to_check):
    print("Valid email address.")
else:
    print("Invalid email address.")
