texto = input('Digite uma frase: ')

lista_palavras_proibidas = ['banana', 'pera', 'maçã', 'uva', 'laranja']
caracteres_de_censura = '💀'



for palavra in lista_palavras_proibidas:
    texto = texto.replace(palavra, caracteres_de_censura * len(palavra))
print(texto)


#len() => Retorna a quantidade de caracteres que há em uma palavra OU a quantidade de elementos que há em uma lista
