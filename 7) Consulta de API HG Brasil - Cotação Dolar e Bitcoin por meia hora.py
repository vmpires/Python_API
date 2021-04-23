import time, threading
import json
import requests

WAIT_SECONDS = 60

def CotarDolar():
    f = open ('config.json', 'r')
    key = json.load(f)
    request = requests.get(f"https://api.hgbrasil.com/finance?format=json-cors&key={(key['key'])}")
    cotacao = dict(request.json())
    return float(cotacao['results']['currencies']['USD']['buy'])

def CotarEuro():
    f = open ('config.json', 'r')
    key = json.load(f)
    request = requests.get(f"https://api.hgbrasil.com/finance?format=json-cors&key={(key['key'])}")
    cotacao = dict(request.json())
    return float(cotacao['results']['currencies']['EUR']['buy'])

def CotarBitcoin():
    f = open ('config.json', 'r')
    key = json.load(f)
    request = requests.get(f"https://api.hgbrasil.com/finance?format=json-cors&key={(key['key'])}")
    cotacao = dict(request.json())
    return float(cotacao['results']['currencies']['BTC']['buy'])

def foo():
    print(time.ctime())
    print(f'Dólar comercial: R$ {CotarDolar():.2f}')
    print(f'Euro comercial: R$ {CotarEuro():.2f}')
    print(f'Bitcoin: R$ {CotarBitcoin():.2f}\n')
    thread1 = threading.Timer(WAIT_SECONDS, foo)
    thread1.start()
    foo.counter += 1
    if foo.counter == 10:
        thread1.cancel()

foo.counter = 0   
foo()