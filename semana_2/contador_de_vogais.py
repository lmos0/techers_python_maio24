# O usuário vai digitar uma palavra e nosso programa vai contar quantas vogais há na palavra

palavra = input('Digite uma palavra: ').lower()

vogais = ['a','e','i','o','u']

quantidade_de_vogais = 0 


for letra in palavra:
    if letra in vogais:
        quantidade_de_vogais += 1

print(f'Há {quantidade_de_vogais} vogais dentro de {palavra}')