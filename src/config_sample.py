# General Configuration
__author__ = 'gdjohn4s'
from src.config import HTML_ENABLE


LOG: str = r'ilovemail.log'

# SMTP Server Auth
MAIL_FROM: str = 'mail@from.com'
MAIL_PWD: str = 'password'
MAIL_TO: str = 'mailto@one.com', 'mailto@two.com'
MAIL_CC: str = ''

# SMTP Options
SMTP_SERVER: str = 'smtp-mail.outlook.com'
SMTP_PORT: int = 587
SSL_ENABLE: bool = True

# Mail Options
SUBJECT: str = 'HELLO'
HTML_ENABLE: bool = True
BODY: str = 'My friend' # -> You can set html here like ''' <html> '''
BODY_FILE_HTML: str = r'body.html'