with open('nomes.txt', 'r') as file:
    linhas = file.readlines()
    for linha in sorted(linhas):
        print(f'Oi, {linha}')