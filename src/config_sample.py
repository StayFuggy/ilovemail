# General Configuration
__author__ = 'gdjohn4s'
__version__ = '2.0.0'
LOG: str = 'ilovemail.log'

# SMTP Server Auth
MAIL_FROM: str = "mail@from.com"
MAIL_PWD: str = "password"
MAIL_TO: str = "mailto@one.com", "mailto@two.com"

# SMTP Options
SMTP_SERVER: str = "smtp-mail.outlook.com"
SMTP_PORT: int = 587
SSL_ENABLE: bool = True

# Mail Options
SUBJECT: str = "HELLO"
BODY: str = "My friend"