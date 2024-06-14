#Sistema de cadastro e consultas

#Desenvolver um programa que simula um sistema de cadastros e consultos de usuários

# A estrutura do cadastro será nome:email

# 1 Cadastrar o usuário: Permitir o cadastro de novos usuários, inserindo o nome

# 2 Permitir a consulta do e-mail cadastrado, digitando apenas o nome do usuário

# 3 Encerrar o programa

cadastros = {}
novo_usuario_email = None
novo_usuario_nome = None

print('Digite 1 para cadastrar um novo usuário e digite 2 para consultar um usuário. Digite 0 para encerrar o programa ')

while True:
    comando = input('Digite a opção desejada: ')

    if comando == "1":
        novo_usuario_email = input('Digite o e-mail do novo usuário ')
        novo_usuario_nome = input('Digite o nome do usuário ')
        cadastros[novo_usuario_nome] = novo_usuario_email
    
    elif comando == '2':
        usuario_consultado = input('Digite o nome do usuário ')
        if usuario_consultado in cadastros:
            print(f'O e-mail do usuário {usuario_consultado} é {cadastros[usuario_consultado]}')
        else:
            print('Usuário não encontrado consultado')
    
    elif comando == '0':
        break

    else:
        print('Comando Inválido ')


