import requests
import json

def BuscaPokemon(poke_input):  
    request = requests.get('https://www.canalti.com.br/api/pokemons.json')
    pokedex = request.json()
    poke_input = (poke_input - 1)
    return pokedex['pokemon'][poke_input]

ListaPoke = []
arquivo  = open ('Lista_Poke.txt','r', encoding='utf-8')
lines = arquivo.read().split('\n')

for line in lines:
    ListaPoke.append(line)

f  = open ('ListaPokeFull.csv','w+', encoding='utf-8')
for line in ListaPoke:
    final = str(f"\t{BuscaPokemon(int(line))['num']};{BuscaPokemon(int(line))['name']};{BuscaPokemon(int(line))['type']}\n")
    f.write(final)
    print(f'Pokemon número {line} sendo adicionado...')

print ('Sua Pokedéx foi criada com sucesso!')
arquivo.close()
f.close()