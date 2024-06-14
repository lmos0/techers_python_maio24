lista_de_nomes = []

for _ in range(3):
    lista_de_nomes.append(input('Digite seu nome: '))


for nome in sorted(lista_de_nomes):
    print(f"Oi, {nome}")


file = open('nomes.txt','a') #Cria uma variável para usar o modo de manipulação de arquivo do Python. Primeiro argumento "diretório/nome do arquivo" e segundo parâmetro é o modo de leitura "w" significa write

file.write(f'{nome}\n') #Escrevendo/criando o arquivo

file.close() #Fechando arquivo para evitar possíveis dores de cabeça

