#str. String são listas de caracteres

palavra = 'batata'
lista_de_compras = ['banana', 'tomate', 'pão']

# print(palavra[0]) # Imprimindo o último elemento da string 
# print(lista_de_compras[0])


#Fatiar strings ou palavras

# print(palavra[2:6])
# print(lista_de_compras[0:3])

lista_de_convidados = ['luís', 'marcela', 'victor', 'mariluce', 'lucas']

convidado = input('Digite seu nome:').lower().strip() #converte a string para letras minusculas
for nome in lista_de_convidados:
    if nome == convidado:
        print('Você pode entrar')
        #Luís != luis  