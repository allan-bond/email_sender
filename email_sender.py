#!/usr/bin/python3

'''
This script is designed to send a email to what ever email address you specify after the completion 
of the code you designate.

Have this file in your folder with the running script and import it using:
import email_sender

then to send an email you just need to use the following:
email_sender.send_email('example@)
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
# getpass will display no input even when the user is typing. If you want a mask such as ***** then you 
# can import stdiomask. It is not part of the base install of python so first you have to install it using
# pip install stdiomask
def send_email(send_address, send_password, rec_address, mes_subject, mes_text):
    '''
    Arguements:
    send_email(send_address, send_password, rec_address, mes_subject, mes_text)
    send_address: email address where you are sending the email from
    send_password: password of the sending email account. If left blank then it will prompt you to enter it in the console but no text will show for security purposes.
    rec_address: email address where you are sending the email to
    mes_subject: the subject of the email
    mes_text: the body of the email

    example:
    send_email('sender@example.com', 'ABCD', 'receiver@example.com', 'Hi', 'Hello')
    '''
    # The mail addresses and password
    if send_address == None:
        sender_address = input('Sender Email Address: ')
    else:
        sender_address = send_address

    if send_password != None:
        sender_password = send_password
    else:
        sender_password = getpass.getpass('Sender Email Password: ')
    
    if rec_address == None:
        receiver_address = input('Receiver Email Address: ')
    else:
        receiver_address = rec_address

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    if mes_subject == None or mes_subject == '':
        message['Subject'] = input('Please enter a subject line: ')
    else:
        message['Subject'] = mes_subject

    # Write the message
    if mes_text != None:
        mail_content = mes_text
    else:
        mail_content = input('Please write your message: ')

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) # gmail with port
    session.starttls() # security
    session.login(sender_address, sender_password) # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

