import json
import requests
import urllib.parse as urlparse

f = open('config.json','r')
key = json.load(f)

address = input('Digite uma localização geográfia(cidade, local, etc): ')
urllatlon = 'https://nominatim.openstreetmap.org/search/'+ urlparse.quote(address) +'?format=json'
response = requests.get(urllatlon).json()

weather = requests.get(f"https://api.hgbrasil.com/weather?key={(key['key'])}&lat={(response[0]['lat'])}&lon={(response[0]['lon'])}&user_ip=remote")
weatherresp = weather.json()

print(f"Cidade: {weatherresp['results']['city']}\nTemperatura atual: {weatherresp['results']['temp']}°\nUmidade do ar: {weatherresp['results']['humidity']}%\nVelocidade do vento: {weatherresp['results']['wind_speedy']}\nObservações: {weatherresp['results']['description']}")

input()