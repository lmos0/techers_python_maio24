
def buscar_numero():

    while True:
        try:
            return int(input('Digite um número: '))
        except ValueError:
            pass #Quando decidimos não tratar uma erro específico do programa, por tratar-se de um ponto crítico da aplicação. Vantagens: Você garante que o programa não vai parar de funcionar. Desvatagens: Fica mais díficl identificar a origem/motivo erro.


x = buscar_numero()
print('O número digitado foi', x)