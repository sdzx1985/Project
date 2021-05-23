from imap_tools import MailBox
from Account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# reverse : True = recent
for msg in mailbox.fetch(limit=1, reverse=True): 
    print("Title", msg.subject)
    print("From", msg.from_)
    print("To", msg.to)
    print("CC", msg.cc)
    print("BCC", msg.bcc)
    print("DATE", msg.date)
    print("Body", msg.text)
    print("HTML message", msg.html)
    print("=" * 20)

    for att in msg.attachments:
        print("Attachments", att.filename) 
        print("Type", att.content_type)
        print("Size", att.size)

        # download
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("Complete {} download".format(att.filename))

mailbox.logout()