import requests 
import json 

cep = input('Digite o CEP a ser consultado: ')
url =   f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url)

print(resposta.status_code)
#print(resposta.json())

print(resposta.json()['logradouro'])
print(resposta.json()['bairro'])
print(resposta.json()['localidade'])
print(resposta.json()['uf'])
