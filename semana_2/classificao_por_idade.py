# **Classificação por Idade:**

# - Crie um programa que receba a idade de uma pessoa e a classifique em uma das seguintes categorias:
#     - Criança: até 12 anos
#     - Adolescente: de 13 a 18 anos
#     - Adulto: de 19 a 64 anos
#     - Idoso: acima de 65 anos
# - Exiba a categoria de classificação da pessoa.

idade = int(input('Digite a idade da pessoa: '))

if idade <= 12:
    print('Criança')
elif idade <=18:
    print('Adolescente')
elif idade <=64:
    print('Adulto')
else:
    print('Idoso')