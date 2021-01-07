# - Configuration file to manage mail configuration

# - Script info
__version__ = '0.0.15'
__author__ = 'gdjohn4s'

# - Login and Send params
mail_from = 'sender email'
mail_to = 'receiver email'
password = 'your password'

# - Subject and body email
SUBJECT = 'HELLO PY'
BODY = 'HELLO FROM PYTHON'

# - Server connection params
# Google SMTP
smtp_server = 'smtp.gmail.com'
port = 465
TLSport = 587

# Outlook SMTP
smtp_outlook = 'smtp.office365.com'
port_outl = 587

# Libero SMTP
smtp_lib = 'smtp.libero.it'
port_lib = 465

# - Configuration params
# - ID list for service identification
# 1) Google
# 2) Outlook
# 3) Libero
id_def_service = '2'
id_services = {'google': '1', 'outlook': '2', 'libero': '3'}
# id_service = ['1', '2', '3']