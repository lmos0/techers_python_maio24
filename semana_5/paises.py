with open('paises.csv', 'r') as arquivo:
    for linha in arquivo:
        coluna = linha.rstrip().split(',')
        print(f'O país {coluna[0]} está no continente {coluna[1]}')
        