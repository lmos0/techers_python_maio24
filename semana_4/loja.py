#Crie um dicionário onde as chaves são itens de uma loja e os valores são os preços. Calcule e imprima a soma de todos os preços.

loja = {
    'camiseta': 90,
    'calça': 150,
    'Sapato': 130
}


valores_loja = loja.values()
total = sum(valores_loja)
print(total)