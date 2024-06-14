

lista_de_compras = ['pão', 'manteiga', 'leite', 'doce de leite'] #o index da lista começa a ser contado a partir do 0. Ou seja, o primeiro elemento está no index '0', e o segundo no index '1'
#print(lista_de_compras[3]) # acessar elementos específicos dentro da lista



# for _ in lista_de_compras:
#     if _ == 'leite':
#         print('Há leite na sua lista')

if 'coca' in lista_de_compras: # O comando 'in' testa se o valor está presente dentro de uma lista
    print('Você ganhou um cupom de R$10,00, por causa da manteiga!')
else:
    print('Sem produto premiado na sua compra')


# for i in lista_de_compras:
#     print('oi')

# i = 0
# while i < 4:
#     print('oi')
#     i+=1