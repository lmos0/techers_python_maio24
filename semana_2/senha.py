#Um programa que vai controlar o login do usuário em um serviço

senha = 'coxinha_123'

senha_digitada = input('Digite sua senha: ')

while senha_digitada != senha:
    print('Senha incorreta! 😒')
    senha_digitada = input('Digite sua senha: ')

print('Usuário logado')