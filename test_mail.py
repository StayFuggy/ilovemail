from smtplib import SMTP

# - Cast response message in list to identify HTTP code
with SMTP('smtp.google.com') as smtp:
    messg = list(smtp.noop())
    print(messg[0])
