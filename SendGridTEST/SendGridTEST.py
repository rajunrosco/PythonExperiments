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


HTML_TEMPLATE = '''
This is just some plain text beforehand


<table role="table" rules="rows" style="border:1px solid #000000;">
    <thead role="rowgroup">
        <tr role="row">
            <td role="columnheader" style="border: 1px solid #000000;"><b>LineID</b></td>
            <td role="columnheader" style="border: 1px solid #000000;"><b>Status</b></td>
            <td role="columnheader" style="border: 1px solid #000000;"><b>Old Script</b></td>
            <td role="columnheader" style="border: 1px solid #000000;"><b>New Script</b></td>
            <td role="columnheader" style="border: 1px solid #000000;"><b>Diff Score</b></td>
            <td role="columnheader" style="border: 1px solid #000000;"><b>Action</b></td>
        </tr>
    </thead>
    <tbody role="rowgroup">
        <tr role="row">
            <td role="cell" style="border: 1px solid #000000;">1</td>
            <td role="cell" style="border: 1px solid #000000;">abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz <span style="background-color:violet">abcdefghijklmnopqrstuvwxyz</span> abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td role="cell" style="border: 1px solid #000000;">os1</td>
            <td role="cell" style="border: 1px solid #000000;">ns1</td>
            <td role="cell" style="border: 1px solid #000000;">abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td role="cell" style="border: 1px solid #000000;">A1</td>
        </tr>
        <tr role="row">
            <td role="cell" style="border: 1px solid #000000;">1</td>
            <td role="cell" style="border: 1px solid #000000;">abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz <span style="background-color:violet">abcdefghijklmnopqrstuvwxyz</span> abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td role="cell" style="border: 1px solid #000000;">os1</td>
            <td role="cell" style="border: 1px solid #000000;">ns1</td>
            <td role="cell" style="border: 1px solid #000000;">abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td role="cell" style="border: 1px solid #000000;">A1</td>
        </tr>
        <tr role="row">
            <td role="cell" style="border: 1px solid #000000;">1</td>
            <td role="cell" style="border: 1px solid #000000;">abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz <span style="background-color:violet">abcdefghijklmnopqrstuvwxyz</span> abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td role="cell" style="border: 1px solid #000000;">os1</td>
            <td role="cell" style="border: 1px solid #000000;">ns1</td>
            <td role="cell" style="border: 1px solid #000000;">abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz</td>
            <td role="cell" style="border: 1px solid #000000;">A1</td>
        </tr>
    </tbody>
</table>

'''

HTML_TABLE = '''
<table role="table">
  <thead role="rowgroup">
    <tr role="row">
      <th role="columnheader">First Name</th>
      <th role="columnheader">Last Name</th>
      <th role="columnheader">Job Title</th>
      <th role="columnheader">Favorite Color</th>
      <th role="columnheader">Wars or Trek?</th>
      <th role="columnheader">Secret Alias</th>
      <th role="columnheader">Date of Birth</th>
      <th role="columnheader">Dream Vacation City</th>
      <th role="columnheader">GPA</th>
      <th role="columnheader">Arbitrary Data</th>
    </tr>
  </thead>
  <tbody role="rowgroup">
    <tr role="row">
      <td role="cell">James</td>
      <td role="cell">Matman</td>
      <td role="cell">Chief Sandwich Eater</td>
      <td role="cell">Lettuce Green</td>
      <td role="cell">Trek</td>
      <td role="cell">Digby Green</td>
      <td role="cell">January 13, 1979</td>
      <td role="cell">Gotham City</td>
      <td role="cell">3.1</td>
      <td role="cell">RBX-12</td>
    </tr>
    <tr role="row">
      <td role="cell">The</td>
      <td role="cell">Tick</td>
      <td role="cell">Crimefighter Sorta</td>
      <td role="cell">Blue</td>
      <td role="cell">Wars</td>
      <td role="cell">John Smith</td>
      <td role="cell">July 19, 1968</td>
      <td role="cell">Athens</td>
      <td role="cell">N/A</td>
      <td role="cell">Edlund, Ben (July 1996).</td>
    </tr>
    <tr role="row">
      <td role="cell">Jokey</td>
      <td role="cell">Smurf</td>
      <td role="cell">Giving Exploding Presents</td>
      <td role="cell">Smurflow</td>
      <td role="cell">Smurf</td>
      <td role="cell">Smurflane Smurfmutt</td>
      <td role="cell">Smurfuary Smurfteenth, 1945</td>
      <td role="cell">New Smurf City</td>
      <td role="cell">4.Smurf</td>
      <td role="cell">One</td>
    </tr>
    <tr role="row">
      <td role="cell">Cindy</td>
      <td role="cell">Beyler</td>
      <td role="cell">Sales Representative</td>
      <td role="cell">Red</td>
      <td role="cell">Wars</td>
      <td role="cell">Lori Quivey</td>
      <td role="cell">July 5, 1956</td>
      <td role="cell">Paris</td>
      <td role="cell">3.4</td>
      <td role="cell">3451</td>
    </tr>
    <tr role="row">
      <td role="cell">Captain</td>
      <td role="cell">Cool</td>
      <td role="cell">Tree Crusher</td>
      <td role="cell">Blue</td>
      <td role="cell">Wars</td>
      <td role="cell">Steve 42nd</td>
      <td role="cell">December 13, 1982</td>
      <td role="cell">Las Vegas</td>
      <td role="cell">1.9</td>
      <td role="cell">Under the couch</td>
    </tr>
  </tbody>
</table>
'''

#set API_KEY env var on computer used to send mail
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

mymessage = Mail()
mymessage.from_email = From('phuong.tran@maggiesoterro.com','Phuong T Tran')
mymessage.to = To('benson_yee@yahoo.com','Benson H Yee')
mymessage.subject = Subject('Text PDF attachment')
mymessage.content = Content(MimeType.html, HTML_TEMPLATE)


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