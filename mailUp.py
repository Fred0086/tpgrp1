import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('tpgrp1-bot@outlook.fr', 'groupe1tpfinal')
fromaddr = 'BitCoin <tpgrp1-bot@outlook.fr>'
toaddrs = ['tpgrp1-destinataire@outlook.fr']
sujet = "BitCoin Evolution"
message = u"""\
Bitcoin Up
"""
msg = """\
From: %s\r\n\
To: %s\r\n\
Subject: %s\r\n\
\r\n\
%s
""" % (fromaddr, ", ".join(toaddrs), sujet, message)
try:
    server.sendmail(fromaddr, toaddrs, msg)
except smtplib.SMTPException as e:
    print(e)
server.quit()