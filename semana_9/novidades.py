def add(a,b):
    result = a + b
    return result


print(add(5,9))

#Funções Anônimas 

adicao = lambda a,b: a+b
variavel_chamada_qualquer_coisa = lambda a,b: a -b

print(adicao(5,8))
print(variavel_chamada_qualquer_coisa(5,3))

numbers = [1,2,3,4,5]

even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))
