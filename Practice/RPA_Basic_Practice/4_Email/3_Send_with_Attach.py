import smtplib
from Account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "This is the test mail" # title
msg["From"] = EMAIL_ADDRESS # send
msg["To"] = "aiden.hyunjae@gmail.com"
msg.set_content("Download")

# MIME type
# msg.add_attachment()
with open("file_menu.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("2019.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("718CB.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="oxtest-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # login
    smtp.send_message(msg)