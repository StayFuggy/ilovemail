from smtplib import SMTP

# - Cast response message in list to identify HTTP code
with SMTP('smtp.google.com') as smtp:
    messg = list(smtp.noop())
    print(messg)


with SMTP('smtp.office365.com') as smtp:
    messg = list(smtp.noop())
    print(messg)


with SMTP('smtp.libero.it') as smtp:
    messg = list(smtp.noop())
    print(messg)


