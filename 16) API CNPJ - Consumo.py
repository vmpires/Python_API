import requests

resposta = input("Digite o número do CNPJ sem pontos, espaços e barra: ")

cnpj_data = requests.get(f'https://cn-pj.tech/api/{resposta}').json()

endereco = cnpj_data['endereco']

print(f"\nCNPJ: {cnpj_data['cnpj']}\n\
Razão Social: {cnpj_data['razao_social']}\n\
Natureza Jurídica: {cnpj_data['natureza_juridica']}\n\
Situação Cadatral: {cnpj_data['situacao_cadastral']}\n\
Início das atividades: {cnpj_data['data_inicio_ativ']}\n\
CNAE Principal: {cnpj_data['cnae_principal']}\n\
Endereço: {endereco['tipo_logadouro']} {endereco['logadouro']}, nº \
{endereco['numero']} - {endereco['complemento']} - {endereco['bairro']} - \
{endereco['municipio']}/{endereco['uf']} - CEP: {endereco['cep']}\n")


