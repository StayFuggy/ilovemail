#!/usr/bin/python3

# -- This script will send mail if an specific event start

import smtplib, ssl
from config import *


# - Obtain the HTTP CODE number from smtp server
def get_http_code(server):
    with smtplib.SMTP(server) as smtp:
        messg = list(smtp.noop())
        messg = str(messg[0])
        if messg == '250' or '200' or '201' or '202':
            return messg
        else:
            raise Exception('Request to: ', server, ' failed')


def provider():
    if id_def_service in id_services.values():
        if id_def_service == '1':
            return smtp_server, TLSport
        elif id_def_service == '2':
            return smtp_outlook, port_outl
        elif id_def_service == '3':
            return smtp_lib, port_lib
    else:
        pass


# ------------------------------------------------------------ #
# -------------------------- MAIN ---------------------------- #
# ------------------------------------------------------------ #

# Create a secure SSL context https://www.youtube.com/watch?v=kFDPsky8UCs
context = ssl.create_default_context()


# - Getting smtp server and port from provider
smtp_server, TLSport = provider()


# - Creating message and ping provider
message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY)
httpcode = get_http_code(smtp_server)
print('SMTP SERVER: OK, CODE: ', httpcode)


# - Creating context with SSL connection
try:
    context = ssl.create_default_context()
except Exception as e2:
    print('Error creating context: ', e2)

# - Trying to send mail with server.sendmail method
with smtplib.SMTP(smtp_server, TLSport) as server:
    try:
        print('Connecting to the server...')
        server.starttls()
        server.login(mail_from, password)
        server.sendmail(mail_from, mail_to, message)
        print('Email sent')
    except Exception as e:
        e = str(e).replace('(', '')
        err = e.split(',')
        if err[0] == '535':
            print('Unauthorized, user or password not match')
        else:
            print('Error sending email, pls check your configuration')
    finally:
        server.quit()
