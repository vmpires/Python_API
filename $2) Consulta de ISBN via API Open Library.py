import requests

def main():
    print('####Consulta-ISBN####')
    isbn_input = input ('Digite o ISBN para a consulta: ')
    if len(isbn_input) != 13:
        print("Quantidade de dígitos inválida!")
        main()
    request = requests.get('https://openlibrary.org/isbn/{}.json'.format(isbn_input))
    if request.status_code == 404:
        print("ISBN não encontrado")
    else:    
        isbn_data = request.json()
        print('Busca realizada com sucesso:')
        print('Nome do livro: {}'.format(isbn_data['title']))
    print ('-------------------------------------------------------') 
    option = int(input('Deseja realizar uma nova consulta?\n1.Sim\n2.Não\n'))
    
    if option == 1:
        main ()
    else:
        exit()
main()