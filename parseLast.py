# This program prints the subject of the most recent email sent to your email
import imaplib
import email
# Connect to inbox
imap_server = imaplib.IMAP4_SSL(host="imap.gmail.com")
myEmail = "raspi.bijesse@gmail.com"
password = input("Type the password for " + myEmail + ": ")
imap_server.login(myEmail, password)
imap_server.select()  # Default is `INBOX`

# Find all emails in inbox
#_, message_numbers_raw = imap_server.search(None, '(FROM "bijesse.thomas@gmail.com")')
_, message_numbers_raw = imap_server.search(None, 'ALL')
id_list = message_numbers_raw[0].split()
#get the most recent email id
latest_email_id = int( id_list[-1] )

for message_number in id_list:
    _, msg = imap_server.fetch(message_number, "(RFC822)")
    # print(msg[0][1]) #prints raw contents of all emails in inbox
#print(latest_email_id)
# Parse the raw email message in to a convenient object
    message = email.message_from_bytes(msg[0][1])


print("Subject: " + message["subject"])

'''
Relevant threads
https://www.devdungeon.com/content/read-and-send-email-python
https://stackoverflow.com/questions/7314942/python-imaplib-to-get-gmail-inbox-subjects-titles-and-sender-name
https://stackoverflow.com/questions/61703194/imap-only-print-data-from-most-recent-email


'''
