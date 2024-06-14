# Dada uma string, conte a frequência de cada caractere usando um dicionário.

texto = 'banana'

frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)