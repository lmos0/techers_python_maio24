
# 1 Receber a idade do usuário
# 2 Se o cliente tiver menos que 18 anos -> Ele não pode locar o carro
# 3 Se o cliente tiver mais de 18 anos, porém menos de 21 anos, ele precisará pagar uma taxa extra
# 4 Se o cliente tiver mais de 21 anos, ele pode alugar o carro normalmente

idade = int(input('Digite sua idade: '))

# if idade >= 21:
   
#     print('Você pode locar o carro')

# elif idade >= 18:
#      print('Você pode alugar o carro, pagando uma taxa extra ')


# else:
#     print('Você não pode alugar o carro')


if idade >= 18 and idade <=21: #18,19,20,21
   
     print('Você pode alugar o carro, pagando uma taxa extra ')

elif idade > 21:
     print('Você pode alugar o carro normalmente')
    
else:
    print('Você não pode alugar o carro')


    #and e #or => spoiler para daqui a pouco 

    # > maior
    # < menor
    # >= maior ou igual
    # <= menor igual
    # == igualdade no sentido de comparação
    # != diferente 

