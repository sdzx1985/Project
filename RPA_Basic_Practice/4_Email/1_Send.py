import smtplib
from Account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # login

    subject = "Test mail" # mail title
    body = "Mail body" # mail body

    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "aiden.hyunjae@gmail.com", msg) # send, recieve, body
