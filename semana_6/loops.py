# Solicita ao usuário um número inteiro positivo
#numero = int(input("Digite um número inteiro positivo para iniciar a contagem regressiva: "))

import time

def countdown(n):
    while n >= 0:
        print(n)
        n = n - 1
        time.sleep(0.5)


#Função que imprime a tabuada de um número usando while até 10.

#Retorno:
#Nenhum

def tabuada(n):
    contador = 1

    while contador <= 10:
        resultado = n * contador
        print(f' {n} x {contador} é = {resultado}')
        contador +=1

numero = int(input("Digite o número que você deseja ver a tabuada: "))

tabuada(numero)


