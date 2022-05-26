import requests
import json
from src.ip import *

token = "f696580631227c10d8b3f42d22b82817"
TipodeConsulta = 1

data = Pegar_ip
id_city = ''


#"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+ iCITY +"&token=your-app-token"

if TipodeConsulta == 1:
    iCITY = data.city
    iURL = f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={iCITY}&token={token}'
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO = json.loads(iRESPONSE.text)
    for iCHAVE in iRETORNO:
        ID = iCHAVE['id']
        Cidade = iCHAVE['name']
        Estado = iCHAVE['state']
        Pais = iCHAVE['country']
        if iCITY == Cidade and data.state == Estado:
            id_city = ID
        print(f'ID: {ID}  Cidade: {Cidade}-{Estado}  País: {Pais}')
    iNEWCITY = id_city

    """
    'http://apiadvisor.climatempo.com.br/api-manager/user-token/:your-app-token/locales' \
            - H 'Content-Type: application/x-www-form-urlencoded' \
            - d 'localeId[]=3477'
    """

    iURL = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{token}/locales'
    payload = f"localeId[]={iNEWCITY}"
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    iRESPONSE = requests.request("PUT", iURL, headers=headers, data=payload)
    TipodeConsulta += 1

if TipodeConsulta == 2:
    iURL = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{iNEWCITY}/current?token={token}"
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO = json.loads(iRESPONSE.text)

    ID = iRETORNO['id']
    name = iRETORNO['name']
    state = iRETORNO['state']
    country = iRETORNO['country']
    data = iRETORNO['data']
    print(f'\nID: {ID}  Cidade: {name}-{state}  País: {country}')
    print(f'Temperatura: {data["temperature"]}')

