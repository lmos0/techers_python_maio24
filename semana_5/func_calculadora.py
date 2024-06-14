#Crie uma função chamada calculadora que receba dois números e uma operação (soma, subtração, multiplicação, divisão) e retorne o resultado da operação.

def calculadora(a:float,b:float,operacao:str):
    if operacao == "soma" or operacao == "+":
        return  a + b
    elif operacao == "subtração" or operacao == "-":
        return a - b
    elif operacao == 'multiplicação' or operacao == "*":
        return a * b
    elif operacao == 'divisão' or operacao == '/':
        return a / b
    else:
        return 'Operação inválida'


x = float(input('Digite um número '))
y = float(input('Digite um número '))
op = input('Digite a operação desejada ')

print(calculadora(x,y,op))