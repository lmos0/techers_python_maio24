import requests 
import json

chave = '35d90404'

filme_consultado = input('Digite o nome do filme que deseja consultar: ')

url = f'https://www.omdbapi.com/?t={filme_consultado}&apikey=35d90404'

resposta = requests.get(url)
data = resposta.json()

if data['Response'] == "True":
    filme = data

    print(f'O filme consultado é {filme['Title']}')
    print(f'O ano de lançamento do filme foi {filme['Year']}')
    print(f'A nota no IMDB é de {filme['imdbRating']}')
    print(f'A direção do filme é feito por {filme['Director']}')
    print(f'O elenco é composto por {filme['Actors']}')
    print(f'País do filme: {filme['Country']}')

else:
    print('Filme não encontrado ou falha na API')


