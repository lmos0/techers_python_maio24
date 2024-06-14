import requests
import json

pokemon_consultado = input('Digite o nome do pokemon a ser consultado: ').lower()

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_consultado}'

resposta = requests.get(url)

print(resposta.status_code)
# informacoes_recebidas = resposta.json()

if resposta.status_code == 200:
    resposta.json()
    print(resposta.json()['name'])
    print(resposta.json()['id'])
else:
    print(f'Falha ao acessar as informações do pokemon {pokemon_consultado}. API devolveu o status {resposta.status_code} ')