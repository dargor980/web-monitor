import requests
import smtplib
import time
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

message = """Se ha dectado una caída en el/los sitio(s) 
https://prismasoftware.cl . Hora de la incidencia: """ + time.strftime("%I:%M:%S")

password = "vllbckfxutrtnbba"
msg['From'] = "german.contrerasa@utem.cl"
msg['To'] = "cafesitomygod@gmail.com"
msg['Subject'] = "Sitio(s) Caido(s)"

msg.attach(MIMEText(message,'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

server.login(msg['From'], password)

server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("Mensaje Enviado")
webAdresses = []
with open('src/sites.json') as file:
    sites = json.load(file)

    for websites in sites['sites']:
        webAdresses.append(websites['url'])

downWebSites = []

while True:

    for req in webAdresses:
        try:

            r = requests.get(req)
            if r.status_code == requests.codes.ok:
                print("OK")
            else:
                downWebSites.append(req)
        except requests.exceptions.RequestException:
            print("URL NO EXISTENTE")
            downWebSites.append(req)
    
   


    if downWebSites:
        print("SITIOS CAIDOS")
    else:
        print("NO SE CAYERON SITIOS EN ESTA ITERACION")
        
    time.sleep(300)

