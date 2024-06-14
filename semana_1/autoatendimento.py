# Escrever um software de autoatendimento 
# Opção 1 Falar com departamento de vendas
# Opção 2 falar com departamento de cobranças
# Opção 3 falar com o suporte técnico 

print('Bem-vindo ao sistema de atendimento automático!')
print('===============================================')
print('Pressione 1 para falar com o departamento de vendas')
print('===============================================')
print('Pressione 2 para falar com o departamento de cobranças')
print('===============================================')
print('Pressione 3 para falar com o suporte técnico')

user_input = input('Digite uma opção (1) (2) (3)! ')

if user_input == "1":
    print('Olá! Bem-vindo ao departamento de vendas. Como podemos te ajudar? ')

elif user_input == "2":
    print('Olá! Para questões financeiras, favor entrar em contato pelo e-mail financeiro@naoestamosnemaipravoce.com.br')
elif user_input == "3":
    print('Olá, aqui é equipe de suporte técnico.\n Se você precisa de suporte para seu serviço de telefone, digite: 1. \n Caso você precise de suporte com a sua internet digite 2.\n Se quiser falar sobre telefonia móvel, digite 3!\n')
    sub_input = input('Digite uma opção (1) (2) (3)! ')
    if sub_input == '1':
        print('Estou aqui para ajudar com o problema no seu telefone')
    elif sub_input == "2": 
        print('Estou aqui para te ajudar com o problema da internet')
    elif sub_input == "3":
        print('Estou aqui para te ajudar com o problema da linha de celular!')
    else:print('Por favor digite uma opção válida! 🤬')


else:
    print('Por favor digite uma opção válida! 🤬')