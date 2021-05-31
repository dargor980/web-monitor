from email.message import EmailMessage
import smtplib, socket
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def parseData(data):
    aux = ""
    for i in data:
        aux += " ".join(i)
    return aux


"""
It sends emails when it detects the incident on the sites specified in sites.json.
To configure the mailing you must modify the following variables:

msg ['From]: your email address that you will use as sender. string

msg ['to']: The receiver email address.

smtplib.SMTP ('your smtp server: port'): for example:

for gmail: smtp.gmail.com: 587

password: your password. For gmail you must configure an application password from the google account settings
"""

def sendEmail(content):
    sites = parseData(content)
    msg = MIMEMultipart()
    print("lista: ", sites)
    message = "Se ha detectado una caída en el/los sitio(s):\n" + sites + "\nFecha y hora de la incidencia: " + time.strftime("%d/%m/%y") + " " + time.strftime("%X")
    password = "vllbckfxutrtnbba"
    msg['From'] = "example@domain.com" 
    msg['To'] = "example2@domain.com"
    msg['Subject'] = "Sitio(s) Caído(s)"
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except socket.error as e:
        print("No se pudo realizar la conexión")

