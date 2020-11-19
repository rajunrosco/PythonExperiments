import base64
import sendgrid
import os
import pyodbc
import PyPDF2
import shutil
import smtplib  

#pip install sendgrid
from sendgrid.helpers.mail import *

# Here are the email package modules we'll need
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TEST_MESSAGE='''
Dear valued stockist,<br>
<br>
To make our delivery service as smooth as possible over the Christmas period please contact me by phone or reply to this email of your planned days of closure to assure we do not attempt to deliver while you are enjoying a well-earned break.<br>
<br>
Please include the following information:<br>
<br>
	<b>Your Customer Account Number:<br>
<br>
	Your Shop Name:<br>
<br>
	The last date you can accept a delivery in 2019:<br>
<br>
	The first date you can accept a delivery in 2020:</b><br>
<br>
<br>
We will be closed 5:00pm ,Monday, December 23rd 2019 and re-open at 9:30am on Thursday January 2nd 2020.<br>
<br>
Kind regards,<br>
<br>
<br>
<br>
Gareth Tipton, Accounts Assistant UK<br>
<a href="mailto:gareth.tipton@maggiesottero.com?subject=re:Maggie Sottero Designs LTD Weekly Dispatch Invoice [TEST]">gareth.tipton@maggiesottero.com</a><br>
Maggie Sottero Designs®<br>
Tel: 0344 324 0324 (Main)<br>
Tel: +44 (0)151 482 3000 (International)<br>
<br>
<br>
'''

TEST_TEMPLATE = '''
<style>
  table, th, td{ border: 1px solid #000000; border-collapse: collapse; }
  th, td{ padding: 8px; }
  tr:nth-child(even) { background-color: #eee; }
</style>
<table role="table" rules="rows">
    <thead role="rowgroup">
        <tr role="row">
            <td><b>LineID</b></td>
            <td><b>Status</b></td>
            <td><b>Old Script</b></td>
            <td><b>New Script</b></td>
            <td><b>Diff Score</b></td>
            <td><b>Action</b></td>
        </tr>
    </thead>
    <tbody role="rowgroup">
        <tr role="row">
            <td>1</td>
            <td>abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz <span style="background-color:violet">abcdefghijklmnopqrstuvwxyz</span> abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td>os1</td>
            <td>ns1</td>
            <td>abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td>A1</td>
        </tr>
        <tr role="row">
            <td>1</td>
            <td>abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz <span style="background-color:violet">abcdefghijklmnopqrstuvwxyz</span> abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td>os1</td>
            <td>ns1</td>
            <td>abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td>A1</td>
        </tr>
        <tr role="row">
            <td>1</td>
            <td>abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz <span style="background-color:violet">abcdefghijklmnopqrstuvwxyz</span> abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td>os1</td>
            <td>ns1</td>
            <td>abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td>A1</td>
        </tr>
    </tbody>
</table>

'''

#set API_KEY env var on computer used to send mail
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

#mymessage = Mail()
myfrom = From('phuong.tran@maggiesoterro.com','Phuong T Tran')
myto = To('benson_yee@yahoo.com','Benson H Yee')
mysubject = Subject('Text PDF attachment')
mycontent = Content(MimeType.html, TEST_MESSAGE+TEST_TEMPLATE)

mymessage = Mail(from_email=myfrom, to_emails=myto, subject=mysubject, html_content=mycontent)

fp = open(r'C:\GitHub\DEV_MAGGIE\Source\MaggieMailer\resource\Test01.pdf', 'rb')
data = fp.read()
fp.close()
# Encode the payload using Base64
dataencoded = base64.b64encode(data).decode()

myattachment = Attachment()
myattachment.file_content = FileContent(dataencoded)
myattachment.file_name = FileName("Test01.pdf")
myattachment.file_type = FileType("application/pdf")
myattachment.disposition = Disposition("attachment")
myattachment.content_id = ContentId("Test PDF")

mymessage.attachment = myattachment


try:
    response = sg.send(message=mymessage)

    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)