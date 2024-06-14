frase = input('Digite seu texto: ')

lista_de_palavras = frase.split('t')
print(lista_de_palavras)

contador = 0

for palavra in lista_de_palavras:
    contador += 1
print('O número de palavra no trecho citado é de ', contador)