import requests, json

f = open('config.json','r')
key = json.load(f)

futapikeytest = key['futapikeytest']
futapikeylive = key['futapikeylive']

campeonato_id = 10

head = {'Authorization': 'Bearer ' + futapikeylive}
data = {'app' : 'aaaaa'}

url = f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}'
response = requests.post(url, json=data, headers=head)
resposta = response.json()

print("\nBem vindo ao app do Brasileirão 2021\n")
print(f"Rodada atual: {resposta['rodada_atual']['nome']}\n")
rodada = input('Digite a rodada que deseja consultar os placares: ')

url = f'https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/rodadas/{rodada}'
response = requests.post(url, json=data, headers=head)
resposta = response.json()

for partida in resposta['partidas']:
    print(partida['placar'])
