#**Par ou Ímpar:**

#- Crie um programa que receba um número inteiro do usuário e verifique se ele é par ou ímpar.
#- Exiba uma mensagem informando se o número é par ou ímpar.

numero_do_usuario = int(input('Digite um número: '))

if numero_do_usuario % 2 == 0: #Se o resto da divisão entre numero_do_usuario e 2 for igual a zero, o número é par
    print('par')
else:
    print('ímpar')
