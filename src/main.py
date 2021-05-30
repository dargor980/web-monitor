import requests
import time
import json
import os
import mailConfig


webAdresses = []
with open('src/sites.json') as file:
    sites = json.load(file)

    for websites in sites['sites']:
        webAdresses.append(websites['url'])

downWebSites = []

mailConfig.sendEmail(downWebSites)
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

