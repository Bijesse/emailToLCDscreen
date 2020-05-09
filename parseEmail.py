# This program reads you the content of each email in your inbox
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

# Find all emails in inbox
_, message_numbers_raw = imap_server.search(None, 'ALL')
for message_number in message_numbers_raw[0].split():
    _, msg = imap_server.fetch(message_number, "(RFC822)")

# Parse the raw email message in to a convenient object
    message = email.message_from_bytes(msg[0][1])

# Print the subject of all messages
    print("Subject: " + message["subject"])

    '''
    print('== Email details =====')
    print(f'From: {message["from"]}')
    print(f'To: {message["to"]}')
    print(f'Cc: {message["cc"]}')
    print(f'Bcc: {message["bcc"]}')
    print(f'Urgency (1 highest 5 lowest): {message["x-priority"]}')
    print(f'Object type: {type(message)}')
    print(f'Content type: {message.get_content_type()}')
    print(f'Content disposition: {message.get_content_disposition()}')
    print(f'Multipart?: {message.is_multipart()}')
    '''
