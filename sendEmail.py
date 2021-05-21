import smtplib
import ssl
from getpass import getpass


login_email = input("Enter login email: ")
login_password = getpass("Enter login password: ")
receiver_email = input("Enter receiver email: ")

subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email(text only): ")

message = f""" 
Subject: {subject}
To: {receiver_email}

{body}
"""

# load the system trusted certificates for SSL connection.
# user need to confirm whether gmail account 'less secure app access' is on or not
context = ssl.create_default_context()

# using gmail smtp server port: 465 for SMTP_SSL and 587 for starttls
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp_obj:
    # gmail needs to authenticate user before email sending
    smtp_obj.login(login_email, login_password) 
    # send the mail.
    smtp_obj.sendmail(login_email, receiver_email, message)
    # at the exit of the with statement, the smtp connection will auto close.
