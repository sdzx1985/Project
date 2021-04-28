import smtplib
from Account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "This is the test mail" # title
msg["From"] = EMAIL_ADDRESS # send
msg["To"] = "aiden.hyunjae@gmail.com"

# to several people
# msg["To"] = "aiden.hyunjae@gmail.com", "aiden.grrrr@gmail.com", "ho2840@email.vccs.edu"
# to_list = ["aiden.hyunjae@gmail.com", "aiden.grrrr@gmail.com", "ho2840@email.vccs.edu"]
# msg["To"] = ", ".join(to_list) 

# CC
# msg["Cc"] = "aiden.hyunjae@gmail.com"

# msg["Bcc"] = "aiden.hyunjae@gmail.com"

msg.set_content("Test mail.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # login
    smtp.send_message(msg)