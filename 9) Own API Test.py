import requests
import json
from requests.auth import HTTPBasicAuth

def BuscaAlunos():
    request = requests.get('http://127.0.0.1:8000/alunos/?format=json',
            auth = HTTPBasicAuth('victorpires', '1234')) 
    alunos = request.json()
    for item in range(3):
        print(f"Id: {alunos[item]['id']}\nNome: {alunos[item]['nome']}\nRG: {alunos[item]['rg']}\nCPF: {alunos[item]['cpf']}\n")

BuscaAlunos()