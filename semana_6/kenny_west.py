import requests
import json

url = 'https://api.kanye.rest'

resposta = requests.get(url)

print(resposta.status_code)
# print(resposta.json())
print(resposta.json()['quote'])