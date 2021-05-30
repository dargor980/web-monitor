from email.message import EmailMessage
import smtplib, socket
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendEmail(content):
    sites = " ".join(content)
    msg = MIMEMultipart()

    message = "Se ha detectado una caída en el/los sitio(s)." + sites + "\nFecha y hora de la incidencia: " + time.strftime("%d/%m/%y") + " " + time.strftime("%X")

    password = "vllbckfxutrtnbba"

    msg['From'] = "german.contrerasa@utem.cl"
    msg['To'] = "cafesitomygod@gmail.com"
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

