import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def check_email(email):
    if re.fullmatch(regex, email):
        confirmation_message = "Thank you for sending your message."
    else:
        print("Invalid e-mail")
        confirmation_message = "Invalid e-mail address, please correct."
    return confirmation_message

def send_email():