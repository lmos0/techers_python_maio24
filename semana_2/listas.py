#Listas são estruturas de dados que armazenam de forma contígua informações dentro de uma variável. 

lista_exemplo = [1,2,3, 'luis', 'texto', False, True, [3,2,1,3], 'luis']

lista_de_compras = ['maçã', 'pera', 'uva', 'banana']

lista_de_numeros = [2,3,99,123123,55,444,3232]

lista_de_compras.append('pão') #Método append SEMPRE adiciona o elemento no FINAL da lista
lista_de_compras.insert(3, 'coca') #Adicionamos um item na posição desejada 
lista_de_compras.pop() #Pop remove o último elemento da lista 
lista_de_compras.remove('pera') #Remove o elemento mencionado como argumento 


lista_de_compras.sort(reverse=True)
print(lista_de_numeros.reverse())

print('quack 🦆\n' * 80)

print(lista_de_compras)
print(lista_de_numeros)
