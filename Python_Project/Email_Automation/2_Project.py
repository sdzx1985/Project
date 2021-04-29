import smtplib
from email.message import EmailMessage
from imap_tools import MailBox
from Account import *
from openpyxl import Workbook

max_val = 3
applicant_list = []

print("[1. Mail Search]")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1
    for msg in mailbox.fetch('(SENTSINCE 28-Apr-2021)'):
        if "Private Event" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            applicant_list.append((msg, index, nickname, phone))
            index += 1

print("[2. Send Mail]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= max_val:
            title = "You are invited"
            content = "Congratulation, {}. \nYou are invited this private event. Your invitation code is {}. Thank you for with us!".format(nickname, phone)
        else:
            title = "Sorry, you were not invited."
            content = "Sorry, {}. You were not invitated this event. \nHowever, you are on the waiting list.(waiting list number : {})".format(nickname, index - max_val)

        msg = EmailMessage()
        msg["subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)

        print("Mail sending to {} is completed.".format(nickname))

print("[3.Create Excel File]")
wb = Workbook()
ws = wb.active
ws.append(["Index", "Name", "Phone"])

for applicant in applicant_list[:max_val]:
    ws.append(applicant[1:])

wb.save("Invited Members.xlsx")

print("Task completed")
