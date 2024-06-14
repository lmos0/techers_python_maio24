import random 

valor_aleatorio = random.randint(1,100)
print(valor_aleatorio)

moeda = random.choice(['cara', 'coroa'])
print(moeda)

baralho = ['rei', 'rainha', 'dama']
random.shuffle(baralho)
for carta in baralho:
    print(carta)