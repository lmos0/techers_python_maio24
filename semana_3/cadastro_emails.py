cadastros = {}

while True:
    nome = input('Digite seu nome (ou digite "sair" para encerrar o programa) ').lower()
    if nome == "sair":
        break
    email = input('Digite seu e-mail ')
    cadastros[nome] = email #Essa linha insere a chave (que está entre []) dentro do dicionário cadastro e associa com um valor (variável e-mail)

#Consultar 

nome_consultado = input('Digite um nome para encontrar o e-mail cadastrado ').lower()
email_cadastrado = cadastros.get(nome_consultado, 'Nome não encontrado')
print(f'Endereço de e-mail de {nome_consultado} é {email_cadastrado}')