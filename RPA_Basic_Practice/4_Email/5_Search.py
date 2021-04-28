from imap_tools import MailBox
from Account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True): # whole mail
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # Call Unread maul
    # for msg in mailbox.fetch('(UNSEEN)'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # From specific
    # for msg in mailbox.fetch('(FROM aiden.hyunjae@gmail.com)', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # Search specific word
    # for msg in mailbox.fetch('(TEXT "test mail")', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # Search Title
    # for msg in mailbox.fetch('(SUBJECT "test mail")', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))    
    
    # for msg in mailbox.fetch(reverse=True): 
    #     if "한품" in msg.subject: # Test other language
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # Search based on the date    
    # for msg in mailbox.fetch('(SENTSINCE 08-Nov-2020)', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(ON 09-Jan-2021)', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # more than 2 options (AND)
    # for msg in mailbox.fetch('(ON 27-Apr-2021 SUBJECT "test mail")', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # at least one option (OR)
    for msg in mailbox.fetch('(OR ON 27-Apr-2021 SUBJECT "test mail")', limit=3, reverse=True): 
        print("[{}] {}".format(msg.from_, msg.subject)) 