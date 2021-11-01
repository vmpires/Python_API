import requests, json
import pandas as pd

f = open('config.json','r')
key = json.load(f)
futapikeytest = key['futapikeytest']
futapikeylive = key['futapikeylive']
campeonato_id = 10
urlroot = "https://api.api-futebol.com.br"
head = {'Authorization': 'Bearer ' + futapikeytest}
data = {'app' : 'aaaaa'}

url = urlroot + f'/v1/campeonatos/{campeonato_id}'
response = requests.post(url, json=data, headers=head)
resposta = response.json()

dictpart1 = {
    "Id_Partida": [],
    "Rodada": [],
    "Placar": [],
    "Time_Mandante": [],
    "Time_Visitante": [],
    "Gols_Mandante": [],
    "Gols_Visitante": [],
    "Data_Realizacao": [],
    "Hora_Realizacao": [],
    "Estadio": [],
    "Posse_de_bola_mandante": [], 
    "Finalizacao_mandante": [],
    "Dribes_mandante": [],
    "Posse_de_bola_visitante": [],
    "Finalizacao_visitante": [],
    "Dribes_visitante": [],
}

for rodada in range(1,2):
    url = urlroot + f'/v1/campeonatos/{campeonato_id}/rodadas/{rodada}'
    response = requests.post(url, json=data, headers=head)
    rodada = response.json()

    for partida in rodada['partidas']:
        urlpartida = urlroot + f"/v1/partidas/{partida['partida_id']}"
        response = requests.post(urlpartida, json=data, headers=head)
        resposta = response.json()
        dictpart1['Id_Partida'] = resposta['partida_id']
        dictpart1['Rodada'] = resposta['campeonato']['rodada_atual']['nome']
        dictpart1['Placar'] = resposta['placar']
        dictpart1['Time_Mandante'] = resposta['time_mandante']['nome_popular']
        dictpart1['Time_Visitante'] = resposta['time_visitante']['nome_popular']
        dictpart1['Gols_Mandante'] = resposta['placar_mandante']
        dictpart1['Gols_Visitante'] = resposta['placar_visitante']
        dictpart1['Data_Realizacao'] = resposta['data_realizacao']
        dictpart1['Hora_Realizacao'] = resposta['hora_realizacao']
        dictpart1['Estadio'] = resposta['estadio']["nome_popular"]
        dictpart1['Posse_de_bola_mandante'] = resposta['estatisticas']['mandante']['posse_de_bola']
        dictpart1['Finalizacao_mandante'] = resposta['estatisticas']['mandante']['finalizacao']['total']
        dictpart1['Dribes_mandante'] = resposta['estatisticas']['mandante']['dribes_bem_sucedidos']
        dictpart1['Posse_de_bola_visitante'] = resposta['estatisticas']['visitante']['posse_de_bola']
        dictpart1['Finalizacao_visitante'] = resposta['estatisticas']['visitante']['finalizacao']['total']
        dictpart1['Dribes_visitante'] = resposta['estatisticas']['visitante']['posse_de_bola']

df = pd.DataFrame(dictpart1, index=[0])

df.to_excel("parte1.xlsx", sheet_name="tabestbr2021", index=False)


    
