import smtplib, ssl
import os
import logging
from config import *
from email.mime.text import MIMEText


# Setting default logging properties
logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        filename=LOG,
        filemode='w')


def check_smtp(server: str) -> bool:
    """
    Return True if smtp server is available
    """
    with smtplib.SMTP(server) as smtp:
        smtp.connect(server)
        messg: list = list(smtp.noop())
        messg: str = str(messg[0])
        if messg == '250' or '200' or '201' or '202':
            return True
        else:
            logging.error(f'Error connecting to {server}')
            raise Exception


def get_context() -> ssl.SSLContext:
    """
    Return the SSL default context
    """
    return ssl.create_default_context()


def send_mail(
    SMTP_SERVER: str,
    SMTP_PORT: str,
    MAIL_FROM: str,
    MAIL_PWD: str,
    MAIL_TO: str,
    message: str
    ) -> bool:
    """
    Check if SSL is enabled in config file, connect to the SMTP server
    and using basic auth send the email defined in config.py
    """
    if SSL_ENABLE == True:
        logging.info("Connecting with SSL Enabled")
        try:
            msg: MIMEText = MIMEText(BODY)
            msg['Subject'] = SUBJECT
            msg['From'] = MAIL_FROM
            msg['To'] = ", ".join(MAIL_TO)
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as mail:
                mail.starttls()
                mail.login(MAIL_FROM, MAIL_PWD)
                mail.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
                logging.info("Email Sent!")
        except Exception as e:
            mail.close()
            logging.error(f'Error sending email {e}')
        finally:
            mail.close()


def main() -> int:
    context: SSLContext = get_context()
    message: str = f'Subject: {SUBJECT}\n\n{BODY}'

    if check_smtp(SMTP_SERVER):
        logging.info(f'Server {SMTP_SERVER} OK - Sending the Email')
        send_mail(
            SMTP_SERVER=SMTP_SERVER,
            SMTP_PORT=SMTP_PORT,
            MAIL_FROM=MAIL_FROM,
            MAIL_PWD=MAIL_PWD,
            MAIL_TO=MAIL_TO,
            message=message
            )
    else:
        logging.error("SERVER KO")


if __name__ == "__main__":
    main()