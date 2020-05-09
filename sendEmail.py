#This program allows you to send an email from the command line
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "raspi.bijesse@gmail.com"  # Enter your address
receiver_email = "raspi.bijesse@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: 2nd message

This is second email sent using Python"""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("raspi.bijesse@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)