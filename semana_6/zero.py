#Crie uma função divisao(a,b) que recebe dois números e retorna o resultado da divisão do primeiro pelo segundo. Utilize try-except para tratar a divisão por zero

def divisao(a,b):
    try:
        resultado = a / b
        return resultado
    except:
        return "Erro: divisão por zero não é permitida" 
    
print(divisao(6,0))

