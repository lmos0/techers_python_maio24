user_name = input("Olá, por favor, digite seu nome:  ")
print(user_name, ', por favor digite sua idade')
user_age = int(input())
if user_age <= 12:
    print ("aqui está o menu kids")
elif user_age <= 18:
    print ("aqui estão as nossas opções para jovens como você")
elif user_age <= 64:
    print ("aqui está o menu adulto")
else:
    print ("aqui está um menu para a melhor idade!!!")