print('Bem-vindo ao nosso sistema atendimento')
print('Para falar com o Comercial, digite 1')
print('Para falar com o Financeiro, digite 2')
print('Para falar com o Suporte, digite 3')

True
False 


while True:
    escolha_cliente = input('Digite a opção desejada: ')
    print('Caso deseje encerrar a chamada, digite "0" ')

    if escolha_cliente == '1':
        print('Comercial')
    elif escolha_cliente == '2':
        print('Financeiro')
    elif escolha_cliente == '3':
        print('Suporte')
    elif escolha_cliente == '0':
        break
    else:
        print('Por favor, digite uma opção válida!')