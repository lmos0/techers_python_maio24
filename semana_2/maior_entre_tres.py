# **Maior entre Três Números:**

# - Crie um programa que receba três números inteiros do usuário e determine qual é o maior entre eles.
# - Exiba o maior número encontrado

# maior_numero = num1

# if num2 > maior_numero:
#     maior_numero = num2

# if num3 > maior_numero:
#     maior_numero = num3

# print('O maior valor digitado foi: ', maior_numero)

num1 = int(input('Digite um número '))
num2 = int(input('Digite um número '))
num3 = int(input('Digite um número '))

if num1 > num2 and num1 > num3:
    print('O maior número é', num1)
elif num2 > num1 and num2 > num3:
    print('O maior número é', num2)
elif num3 > num1 and num3 > num2:
    print('O maior número é', num3)
else:
    print('Há valores repetidos')