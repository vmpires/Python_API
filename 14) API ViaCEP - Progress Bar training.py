import requests
import datetime
from tqdm import tqdm

def main():
    inicio = datetime.datetime.now()
    cep_input = "090410"
    dictceps = {"CEP":[], "Logradouro":[], "Complemento":[], "Bairro":[], "Cidade":[], "UF": []}

    for i in tqdm(range(30,51)):
        request = requests.get(f'https://viacep.com.br/ws/{cep_input}{i}/json/')
        adress_data = request.json()

        if 'erro' not in adress_data:
            dictceps["CEP"].append(adress_data['cep'])
            dictceps["Logradouro"].append(adress_data['logradouro'])
            dictceps["Complemento"].append(adress_data['complemento'])
            dictceps["Bairro"].append(adress_data['bairro'])
            dictceps["UF"].append(adress_data['uf'])
        else:
            dictceps["CEP"].append("Inválido")
            dictceps["Logradouro"].append("Inválido")
            dictceps["Complemento"].append("Inválido")
            dictceps["Bairro"].append("Inválido")
            dictceps["UF"].append("Inválido")
    
    fim = datetime.datetime.now()
    execucao = fim-inicio
    print(dictceps)
    print("Tempo de execução: ",execucao)

if __name__ == "__main__":
    main()