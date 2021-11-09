import requests
import json

def BuscaISBN(ISBN):  
    request = requests.get('https://openlibrary.org/isbn/{}.json'.format(ISBN)) 
    isbn_data = request.json()
    return isbn_data['title']

ListaISBN = []
arquivo  = open ('ISBN_List.txt','r', encoding='utf-8')
lines = arquivo.read().split('\n')

for line in lines:
    ListaISBN.append(line)

f  = open ('ISBN2.csv','w+', encoding='utf-8')
for line in ListaISBN:
    nome = BuscaISBN(int(line))
    final = (f'\t{line} ; {nome}\n')
    f.write(final)
arquivo.close()
f.close()