import requests

def main():
    print('####Consulta-CEP####')
    cep_input = input ('Digite o CEP para a consulta: ')
    if len(cep_input) != 8:
        print("Quantidade de dígitos inválida!")
        exit()
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    adress_data = request.json()

    if 'erro' not in adress_data:
        print('Busca realizada com sucesso:')
        print('CEP: {}'.format(adress_data['cep']))
        print('Logradouro: {}'.format(adress_data['logradouro']))
        print('Complemento: {}'.format(adress_data['complemento']))
        print('Bairro: {}'.format(adress_data['bairro']))
        print('Cidade: {}'.format(adress_data['localidade']))
        print('UF: {}'.format(adress_data['uf']))
    else:
        print('CEP Inválido!')
    print ('-------------------------------------------------------') 
    option = int(input('Deseja realizar uma nova consulta?\n1.Sim\n2.Não\n'))
    
    if option == 1:
        main ()
    else:
        exit()

main()