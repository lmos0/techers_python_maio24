#Crie um programa que solicita ao usuário que insira várias notas (valores entre 0 e 10). 

soma_das_notas = 0
contador_de_atividades = 0 #a gente vai controlar a quantidade de "provas" que foram adicionadas ao total da nota
media_notas = None #None significa ausência de valor
while True:
    nota = float(input('Digite uma nota (ou um valor negativo para calcular a média digitada)\n'))

    if nota < 0:
        break 

    if 0 <= nota <= 10:
        soma_das_notas += nota #soma_das_notas = soma_das_notas + nota
        contador_de_atividades += 1
    else:
        print('Nota Inválida. Insira um valor entre 0 e 10')

if soma_das_notas > 0:
    media_notas = soma_das_notas / contador_de_atividades
    print('A média das notas inseridas é:', media_notas)

else:
    print('Nenhuma nota válida foi inserida')


#O programa deve continuar pedindo notas até que o usuário insira um valor negativo. 


#Em seguida, exiba a média das notas válidas inseridas.