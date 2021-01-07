#!/usr/bin/python3

# -- This script will send mail if an specific event start

import smtplib, ssl
from environs import Env
from rich import *
from rich.console import Console

console = Console()

# - Obtain the HTTP CODE number from smtp server
def get_http_code(server):
    with smtplib.SMTP(server) as smtp:
        smtp.connect(server)
        messg = list(smtp.noop())
        messg = str(messg[0])
        if messg == '250' or '200' or '201' or '202':
            return messg
        else:
            raise Exception('Request to: ', server, ' failed')


# ------------------------------------------------------------ #
# -------------------------- MAIN ---------------------------- #
# ------------------------------------------------------------ #
if __name__ == '__main__':
    # - Reading .conf environment variables
    try:
        env = Env()
        env.read_env(".conf", recurse=False)
    except Exception as e:
        console.log("Error reading configuration file")

    # - Getting parameters from .conf file
    MAIL_FROM = env.str("mail_from")
    MAIL_TO = env.str("mail_to")
    MAIL_PASSWORD = env.str("password")
    SUBJECT = env.str("SUBJECT")
    BODY = env.str("BODY")
    SMTP_SERVER = ''
    TLSPORT = 0
    id_services = {'google': '1', 'outlook': '2', 'libero': '3'} # Deleted from .conf, get an error while calling a dict with environ

    # Create a secure SSL context https://www.youtube.com/watch?v=kFDPsky8UCs
    context = ssl.create_default_context()

    # - Getting smtp server and port from provider
    # smtp_server, TLSport = provider(id_services)
    if env.str("id_def_service") in id_services.values():
        if env.str("id_def_service") == '1':
            SMTP_SERVER = env.str("smtp_server")
            TLSPORT = env.int("TLSport")
        elif env.str("id_def_service") == '2':
            SMTP_SERVER = env.str("smtp_outlook")
            TLSPORT = env.int("port_outl")
        elif env.str("id_def_service") == '3':
            SMTP_SERVER = env.str("smtp_lib")
            TLSPORT = env.int("port_lib")

    # - Creating message and ping provider
    message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY)
    httpcode = get_http_code(SMTP_SERVER)
    #print(f'[green]SMTP SERVER: OK, CODE: {httpcode}[/green]')

    # - Creating context with SSL connection
    try:
        context = ssl.create_default_context()
    except Exception as e2:
        print('Error creating context: ', e2)

    # - Trying to send mail with server.sendmail method
    with smtplib.SMTP(SMTP_SERVER, TLSPORT) as server:
        try:
            console.status("[bold green]Sending email...")
            console.log('[yellow]Connecting to the server...[yellow]')
            server.starttls()
            server.login(MAIL_FROM, MAIL_PASSWORD)
            server.sendmail(MAIL_FROM, MAIL_TO, message)
            console.log('[bold green]Email sent[/bold green]')
        except Exception as e:
            e = str(e).replace('(', '')
            err = e.split(',')
            if err[0] == '535':
                console.log('[bold red]Unauthorized, user or password not match[/bold red]')
            else:
                console.log('[bold red]Error sending email, pls check your configuration[/bold red]')
        finally:
            server.quit()
