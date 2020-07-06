# Import necessary libraries for communication and display use
import lcddriver
import time
import imaplib
import email

display = lcddriver.lcd()

#wipe LCD screen before printing something new
display.lcd_clear()

def long_string(display, text = '', num_line = 1, num_cols = 20):
	""" 
	Parameters: (driver, string to print, number of line to print, number of columns of your display)
	Return: This function send to display your scrolling string.
	"""
	if(len(text) > num_cols):
		display.lcd_display_string(text[:num_cols],num_line)
		time.sleep(1)
		for i in range(len(text) - num_cols + 1):
			text_to_print = text[i:i+num_cols]
			display.lcd_display_string(text_to_print,num_line)
			time.sleep(0.2)
		time.sleep(1)
	else:
		display.lcd_display_string(text,num_line)
time.sleep(1)
		
while True:
	#Connect to inbox
	imap_server = imaplib.IMAP4_SSL(host="imap.gmail.com")
	myEmail = "xxxxxx"
	password = "xxxxxx"
	imap_server.login(myEmail, password)
	imap_server.select() #INBOX selected by default
	
	#Finds all messages in inbox
	_, message_numbers_raw = imap_server.search(None, 'ALL')
	id_list = message_numbers_raw[0].split()
	#get the most recent email id
	latest_email_id = int( id_list[-2] )

	for message_number in id_list:
		_, msg = imap_server.fetch(message_number, "(RFC822)")
		#Parse raw email message into readable object
		message = email.message_from_bytes(msg[0][1])
		subject = message["subject"]
		fromEmail = message["from"]
		#divide senders email by spaces 
		fromSplit = fromEmail.split(' ')
	
	lcd_line_1 = subject
	lcd_line_2 = fromSplit[0]
		
	long_string(display, lcd_line_1 + "   ", 1)
	# An example of infinite scrolling text
	long_string(display, lcd_line_2 + "      ", 2)	
	
	#display.lcd_clear()
