import smtplib, ssl
import os
import logging
from config import *
from email.mime.text import MIMEText


"""
Name: ilovemail
Author: gdjohn4s
Version: v2.1.4
"""

# Setting default logging properties
logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        filename=LOG,
        filemode='a')


def check_file(filename: str) -> bool:
    """
    Check if body.html exist than return True if exist otherwise false
    """
    path: str = os.getcwd()
    files: list = os.listdir(path)

    if filename in files:
        return True
    else:
        return False


def get_html(filename: str) -> str:
    """
    Get all body html file content and append to a string
    """
    bodyHTML = str()

    if check_file(filename):
        with open(filename, 'r') as bfile:
            bfile.seek(0)
            for line in bfile:
                bodyHTML += line
            return bodyHTML
    else:
        logging.error(f"Can't open {filename}, probably doesn't exist")
        exit(1)


def check_smtp(server: str) -> bool:
    """
    Return True if smtp server is available
    """
    with smtplib.SMTP(server) as smtp:
        smtp.connect(server)
        messg: list = list(smtp.noop())
        messg: str = str(messg[0])
        if messg == '250' or '200' or '201' or '202':
            logging.info(f'Server {SMTP_SERVER} OK {messg} - Checking SSL Encryption')
            return True
        else:
            logging.error(f'Error connecting to {server}')
            raise Exception


def get_context() -> ssl.SSLContext:
    """
    Return the SSL default context
    """
    return ssl.create_default_context()


def send_mail() -> bool:
    """
    Check if SSL is enabled in config file, connect to the SMTP server
    and using basic auth send the email defined in config.py
    """
    if SSL_ENABLE:
        logging.info("Connecting with SSL Enabled")
        try:
            if HTML_ENABLE:
                logging.info("HTML Mime Enabled, getting the body")
                msg: MIMEText = MIMEText(get_html(BODY_FILE_HTML), 'html')
            else:
                logging.info("HTML Mime Disabled, using normal message as body")
                msg: MIMEText = MIMEText(BODY)
            msg['Subject'] = SUBJECT
            msg['From'] = MAIL_FROM
            msg['To'] = MAIL_TO
            msg['Cc'] = MAIL_CC
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as mail:
                mail.starttls()
                mail.login(MAIL_FROM, MAIL_PWD)
                mail.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
                logging.info("Email Sent!")
                mail.close()
        except Exception as e:
            logging.error(f'Email not sent {e}')
        finally:
            mail.close()
    else:
        logging.warning("SSL Connection disabled, for your security, the script will terimnated!")
        exit(1)

def main():
    """
    Main controller function
    """
    context: ssl.SSLContext = get_context()

    if check_smtp(SMTP_SERVER):
        send_mail()
    else:
        logging.error(f'Server {SMTP_SERVER} KO - not responding')


if __name__ == "__main__":
    main()
