import requests
import time
import json
import os
import mailConfig
import http_Errors


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
                description = http_Errors.getCodeErrorDescription(r.status_code)
                downWebSites.append([req," - Error: " + str(r.status_code) + ": " + description + "\n"])
        except requests.exceptions.RequestException:
            print("URL NO EXISTENTE")
            downWebSites.append([req, " - Error: DNS_PROBE_FINISHED_NXDOMAIN\n"])
    if downWebSites:
        print("SITIOS CAIDOS")
        mailConfig.sendEmail(downWebSites)
        downWebSites = []
    else:
        print("NO SE ENCONTRARON INCIDENCIAS EN ESTA ITERACION")
    time.sleep(300)

