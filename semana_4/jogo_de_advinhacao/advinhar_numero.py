from gerar_numero_secreto import gerar_numero_secreto

def advinhar_numero():
    numero_sorteado = gerar_numero_secreto()
    tentativas = 0 

    while True:
        chute = int(input('Digite um número: '))
        tentativas += 1 
        
        if chute == numero_sorteado:
            print(f'Parabéns, você acertou em {tentativas} tentativas')
            break

        elif chute < numero_sorteado:
            print('Tente um número maior!')
        
        else:
            print('Tente um número menor')