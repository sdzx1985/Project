import smtplib
from random import *
from Account import *
from email.message import EmailMessage

nicknames = ["John", "Aiden", "Crystal", "Chelsea", "Mike"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "Invitation of Private Event"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "aiden.hyunjae@gmail.com"

        # content = nuckname + "/" + str(randint(1000, 9999))
        content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        
        smtp.send_message(msg)
        
        print("Email from " + nickname)
