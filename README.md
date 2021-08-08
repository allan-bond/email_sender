# email_sender
 Python code to send an email to yourself when your code is done or has an error.

## Importing
Have the file email_sender.py in the same folder as you have the script you want to use then

import email_sender

## Arguements:
* send_email(send_address, send_password, rec_address, mes_subject, mes_text)
* send_address: email address where you are sending the email from
* send_password: password of the sending email account. If left blank then it will prompt you to enter it in the console with ****** mask.
* rec_address: email address where you are sending the email to
* mes_subject: the subject of the email
* mes_text: the body of the email

## example:
>>> send_email('sender@example.com', 'ABCD', 'receiver@example.com', 'Hi', 'Hello')

If using it from outside the email_sender.py file then after import the code would be:

>>> email_sender.send_email('sender@example.com', 'ABCD', 'receiver@example.com', 'Hi', 'Hello')

If you leave any field blank (think password) then it will ask you for input via the command line. Password will be blank as you type for security.
