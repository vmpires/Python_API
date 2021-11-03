import requests, json
import pandas as pd

f = open('config.json','r')
key = json.load(f)
futapikeytest = key['futapikeytest']
futapikeylive = key['futapikeylive']
campeonato_id = 10
urlroot = "https://api.api-futebol.com.br"
head = {'Authorization': 'Bearer ' + futapikeylive}
data = {'app' : 'aaaaa'}

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

for rodada in range(1,11):
    url = urlroot + f'/v1/campeonatos/{campeonato_id}/rodadas/{rodada}'
    response = requests.post(url, json=data, headers=head)
    rodada = response.json()

    for partida in rodada['partidas']:
        urlpartida = urlroot + f"/v1/partidas/{partida['partida_id']}"
        response = requests.post(urlpartida, json=data, headers=head)
        resposta = response.json()
        dictpart1['Id_Partida'].append(resposta['partida_id'])
        dictpart1['Rodada'].append(resposta['campeonato']['rodada_atual']['nome'])
        dictpart1['Placar'].append(resposta['placar'])
        dictpart1['Time_Mandante'].append(resposta['time_mandante']['nome_popular'])
        dictpart1['Time_Visitante'].append(resposta['time_visitante']['nome_popular'])
        dictpart1['Gols_Mandante'].append(resposta['placar_mandante'])
        dictpart1['Gols_Visitante'].append(resposta['placar_visitante'])
        dictpart1['Data_Realizacao'].append(resposta['data_realizacao'])
        dictpart1['Hora_Realizacao'].append(resposta['hora_realizacao'])
        dictpart1['Estadio'].append(resposta['estadio']["nome_popular"])
        dictpart1['Posse_de_bola_mandante'].append(resposta["estatisticas"]["mandante"]["posse_de_bola"])
        dictpart1['Finalizacao_mandante'].append(resposta["estatisticas"]["mandante"]['finalizacao']['total'])
        dictpart1['Dribes_mandante'].append(resposta["estatisticas"]["mandante"]['dribes_bem_sucedidos'])
        dictpart1['Posse_de_bola_visitante'].append(resposta["estatisticas"]["visitante"]["posse_de_bola"])
        dictpart1['Finalizacao_visitante'].append(resposta["estatisticas"]["visitante"]['finalizacao']['total'])
        dictpart1['Dribes_visitante'].append(resposta["estatisticas"]["visitante"]["posse_de_bola"])

df = pd.DataFrame(dictpart1, index=[0])

    
