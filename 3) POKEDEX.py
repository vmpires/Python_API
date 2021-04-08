import json
import requests

#class pokedex (object):
#pokedex = []
#def recuperar_valor(lista, chave):
   # for valor in lista:
       # if chave in valor:
          #  poke_id = valor[chave]

def main ():
    print ('*****OLÁ TREINADOR, BEM-VINDO À POKEDEX!*****')
    poke_input = int(input ('Digite um número de Pokémon de 1 a 151: '))
    if poke_input < 1 or poke_input > 151:
        print('Amigo, esse programa é só pros raiz, tente novamente.')
        print('-----------------------------------------------------------')
        main ()
    else:
        request = requests.get('https://www.canalti.com.br/api/pokemons.json')
        pokedex = request.json()
        poke_input = (poke_input - 1)
        print (f"Pokemón localizado!\nNúmero: {pokedex['pokemon'][poke_input]['num']}")
        print (f"Nome: {pokedex['pokemon'][poke_input]['name']}")
        print (f"Tipo: {pokedex['pokemon'][poke_input]['type']}")
        print (f"Fraquezas: {pokedex['pokemon'][poke_input]['weaknesses']}")

main ()