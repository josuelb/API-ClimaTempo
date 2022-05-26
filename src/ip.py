from urllib.request import urlopen
import requests


class Pegar_ip:
    #pegando o IP informado como argumento
    ip = str(requests.get('https://api.ipify.org/').text)

    if ip:
        #url do api
        url = f"http://ip-api.com/json/{ip}"

        #Iniciando o request
        request = urlopen(url)
        data = request.read().decode()

        #Convertendo string api para DICT
        data = eval(data)

        city = data['city']
        state = data['region']

    else:
        print('ERROR')
