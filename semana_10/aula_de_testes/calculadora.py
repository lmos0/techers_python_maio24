#escrever um programa com pelo menos 3 funções diferentes
# e escrever um teste pra esse programa 

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError ('Não pode ser dividido por zero')
    return a/b

