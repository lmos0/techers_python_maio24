#Crie uma função chamada media que recebe uma lista de números e retorna a média desses números.

def media(lista_de_numeros): 
    return sum(lista_de_numeros)/len(lista_de_numeros)



lista_do_usuario = []
while True:
    notas = float(input('Digite o valor da nota! Digite "0" para encerrar o programa \n'))
    if notas == 0:
        break
    else:
        lista_do_usuario.append(notas)


print(media(lista_do_usuario))