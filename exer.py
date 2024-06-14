#Criar um programa que recebe um input do usuário
# E o programa deve dizer se o número digitado é maior ou menor que 5

resposta_usuario = int(input('Digite um número: '))

if resposta_usuario > 5:
    print('O número escolhido é maior que 5')

elif resposta_usuario < 5:
    print('O número escolhido é menor que 5')

else:
    print('O número escolhido foi 5')