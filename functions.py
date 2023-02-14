import re
import smtplib
import ssl

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def check_email(email):
    if re.fullmatch(regex, email):
        confirmation_message = "Thank you for sending your message."
    else:
        print("Invalid e-mail")
        confirmation_message = "Invalid e-mail address, please correct."
    return confirmation_message


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "edyta.zelazny01@gmail.com"
    password = "rumgavdnbjwnaljf"
    context = ssl.create_default_context()
    receiver = username

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
