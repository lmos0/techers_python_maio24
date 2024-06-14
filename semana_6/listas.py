#Soma os valores de dentro de uma lista. Vamos usar uma função que vai receber como parâmetro uma lista

def soma_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento #soma = soma + elemento
    return soma


#loop for é utilizado para percorrer um intervalo definido ex:tamanho de lista, tamanho de dicionário, tamanho de string

#loop while é utilizado enquanto uma condição for verdadeira. Ou seja, eu não não tenho um intervalo pré-definido, é necessário que a condição deixe de ser verdadeira

lista_do_usuario = []

# while True:

#     elemento_do_usuario = float(input('Digite um número a ser somado (Digite um número negativo para encerrar o programa) '))

#     if elemento_do_usuario < 0:
#         break

#     else:
#         lista_do_usuario.append(elemento_do_usuario)

# print(soma_lista(lista_do_usuario))


#Escrever uma função que recebe uma lista e calcula a média dos elementos dentro desta lista

def media_lista(lista):
    soma = 0
    #quantidade_de_elementos = 0
    for elemento in lista:
        soma += elemento
        #quantidade_de_elementos +=1
    return soma / len(lista)

lista = [3,6,8]
print(media_lista(lista))