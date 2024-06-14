#Crie uma função acessar_elemento(lista, indice) que recebe uma lista e um índice, e retorna o elemento da lista no índice especificado. Utilize try-except para tratar índices fora do intervalo válido da lista.

def acessar_elemento(lista:list,indice:int):
    try:
        return lista[indice]
    except:
        return "Erro: Índice não existente" 


listinha_de_compras = []

while True:
    item_da_lista = input('Digite um item para ser acrescentado à lista. Quando terminar insira "0" ')
    if item_da_lista != "0":
        listinha_de_compras.append(item_da_lista)
    else:
        break

indice_a_ser_verificado = int(input('Digite o índice o qual você deseja consultar '))

