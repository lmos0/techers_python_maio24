
#   Função que verifica se um número é maior, menor ou igual a outro.

#   Argumentos:
#     x: O primeiro número.
#     y: O segundo número.

#   Retorno:
#     Uma string que indica se x é maior, menor ou igual a y.

#Efeito Colateral e Retorno

def maior_menor_igual(a:int,b:int):
    if a > b:
        return f'{a} é maior que {b}'
    elif b > a:
        return f'{b} é maior que {a}'
    else: 
        return 'Os dois valores são iguais!'


numero1 = int(input('Digite o primeiro valor a ser comparado: '))
numero2 = int(input('Digite o segundo valor a ser comparado: '))

resultado = maior_menor_igual(numero1,numero2)
print(resultado)