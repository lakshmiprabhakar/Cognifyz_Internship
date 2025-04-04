import re

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9,_%+-]+@[a-zA-Z0-9,-]+\.[a-zA-Z]{2,}$'
    match = re.match(email_pattern, email)

    return match is not None

test_emails = [
    'user@example.com',
    'user123@domain.co.uk',
    'user.name@company.com',
    'user@123.456',
    'invalid.email',
    '@missingusername.com',
    'user@invalid_domain',
]

for email in test_emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is NOT a valid email address.")
    