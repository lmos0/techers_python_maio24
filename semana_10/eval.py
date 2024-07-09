# user_input = input('Digite sua operação: ')
# resultado = eval(user_input)

# print(resultado)


add = lambda x, y: x+y
print(add(2,3))

numeros = [1,2,3,4,5]

pares = filter(lambda x:x % 2 == 0, numeros)
print(list((pares)))