#Escrever uma função que vai receber uma string com um texto e essa função vai checar qual é a palavra mais longa (com maior número de caracteres) dentro do texto e retornar essa palavra

def mais_longo(frase):
    frase_filtrada = frase.split(' ')
    palavra_mais_longa = ""

    for palavra in frase_filtrada:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra
    return palavra_mais_longa

#print(mais_longo('Escrever uma função que vai receber uma string com um texto'))

print(mais_longo('Escrever uma função que vai receber uma string com um texto e essa função vai checar qual é'))
