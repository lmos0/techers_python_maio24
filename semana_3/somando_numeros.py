### **Exercício 1: Somando Números até Zero**

# Crie um programa que solicita ao usuário que insira números **continuamente** **até que o usuário insira o número zero**. O programa deve então **exibir a soma de todos os números inseridos** (excluindo o zero).

soma = 0 


# insira números **continuamente** 
while True:
    numero_recebido = int(input('Digite um número para ser somado. Caso deseje interromper o programar, digite "0"\n'))

    if numero_recebido == 0:
        break # Força a saída do loop

    soma = soma + numero_recebido

print('A soma dos números digitados é:', soma)