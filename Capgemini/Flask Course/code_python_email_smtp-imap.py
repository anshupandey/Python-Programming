# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:50:49 2021

@author: anshu
"""

# Python for Emails

## Sending email using SMTP protocol with python

import smtplib
import ssl

message = """
Hey Anshu,
Hope you are doing good today.
See you tomorrow.
Thanks & Regards
"""

server_add = "smtp.gmail.com"
port = 465
sender = "aashishpandeyiot@gmail.com"
receiver= "aashishpandeyiot@gmail.com"
password = input('Enter you password here ')

print("Thank you for password")

context = ssl.create_default_context()

# using smtplib to send emails

server = smtplib.SMTP_SSL(server_add,port,context=context)
server.login(sender,password)
server.sendmail(sender,receiver,message)
server.close()

###################################

from email.message import EmailMessage

message = """
Hey Anshu,
Hope you are doing good today.
See you tomorrow.
Thanks & Regards
"""


msg = EmailMessage()
msg.set_content(message)
msg['Subject']= "new Email from Anshu"
msg['From'] = "aashishpandeyiot@gmail.com"
msg['To'] = "aashishpandeyiot@gmail.com"
user = "aashishpandeyiot@gmail.com"
password = input("password: ")
server = smtplib.SMTP_SSL(server_add,port,context=context)
server.login(user,password)
server.send_message(msg)
server.close()

#################################################

# Receive email using IMAP 

import imaplib
import ssl

host = "imap.gmail.com"
port = 993
username = "aashishpandeyiot@gmail.com"
password = input('Enter you password here ')

print("Thank you for password")

context = ssl.create_default_context()

server = imaplib.IMAP4_SSL(host,port)
server.login(username,password)
server.select("Inbox")
tmp,data = server.search(None,'All')
len(data)
data[0]
data[0].split()
ind = data[0].split()[0]
print(ind)
tmp,mydata = server.fetch(ind,"(RFC822)")

type(mydata)
len(mydata)
type(mydata[0])
len(mydata[0])
print(mydata[0][1].decode())

############################################

#################################################

import imaplib
import ssl

host = "imap.gmail.com"
port = 993
username = "aashishpandeyiot@gmail.com"
password = input('Enter you password here ')

print("Thank you for password")

context = ssl.create_default_context()

server = imaplib.IMAP4_SSL(host,port)
server.login(username,password)
server.select("Inbox")

tmp,data = server.search(None,'ALL')
mail_ids = data[0].split()
mail_ids

# accessing 0th email
tmp,firstmail  = server.fetch(mail_ids[-1],'(RFC822)')   

type(firstmail[0])

import email
message = email.message_from_bytes(firstmail[0][1])

print(message['from'])
print(message['subject'])
message.keys()
for k,v in message.items():
    print(k," : ",v)
    
    
for part in message.walk():
    filename = part.get_filename()
    print(filename)
    if bool(filename):
        file = open(filename,'wb')
        file.write(part.get_payload(decode=True))
        file.close()