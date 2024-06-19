import requests 

api_key = '5738ebfb04d69d4df99d102275978e92'
cidade = input('Digite o nome da cidade a ser consultada: ')


url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric'

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    dados_principais = dados['main']
    descricao_ceu = dados['weather'][0]
  
    
    temperatura = dados_principais['temp']
    umidade = dados_principais['humidity']
    ceu = descricao_ceu['description']

    print(f'Cidade: {cidade}')
    print(f'Temperatura: {temperatura}')
    print(f'Descrição: {ceu}')
    print(f'Umidade de {umidade}%')
else:
    print('Não foi possível completar a requisição! ')
