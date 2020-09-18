import os
import smtplib, ssl
import sys

########################################################################################################################
# This script works on a Gmail account that has been set up to "Allow less secure apps to ON". 
# Be aware that this makes it easier for others to gain access to your account.  That is why it is prudent not to use
# your personal email accounts to test this.  Create an account only to use with scripts such as this

port = 465  # For SSL
password = os.environ.get("GMAILBOTPASS") # Gmail bot password from env var
sender_email = os.environ.get("GMAILBOT") # Gmail bot address from env var
receiver_email = os.environ.get("GMAILBOT_TO") # Enter receiver address (in this case an email to text number address)

if password is None or sender_email is None or receiver_email is None:
    print("[ERROR] Missing arguments")
    sys.exit(1)

message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)