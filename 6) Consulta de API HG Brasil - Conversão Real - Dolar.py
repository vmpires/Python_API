import json
import requests

def CotarDolar(valor_real):
    request = requests.get('https://api.hgbrasil.com/finance?format=json-cors&key=cdfa218e')
    cotacao = dict(request.json())
    conversao = valor_real / float(cotacao['results']['currencies']['USD']['buy'])
    return conversao


valor_real = input('Digite um valor em Real(R$): ')
if ',' in valor_real:
    valor_real = float(valor_real.replace(',','.'))
    print (f'Dólar (USD): U$ {CotarDolar(valor_real):.2f}')
else:
    valor_real = float(valor_real)
    print (f'Dólar (USD): U$ {CotarDolar(valor_real):.2f}')