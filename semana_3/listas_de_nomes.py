#Crie um programa que permita ao usuário inserir 5 nomes em uma lista e depois exiba esses nomes em ordem alfabética.

lista_de_nomes = ['luis', 'lucas', 'mariluce', 'victor', 'marcela']

# for i in range(5):
#     nome = input('Digite um nome: ')
#     lista_de_nomes.append(nome)

lista_de_nomes.sort()
print(lista_de_nomes)