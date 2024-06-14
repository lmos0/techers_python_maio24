convidados = ['Alice', 'Lucas', 'Victor', 'Mariluce', 'Luís', 'Taís']

nome_a_ser_buscado = input('🤖 Por favor, me informe o seu nome, para que eu possa checar na lista de convidados: ')

if nome_a_ser_buscado in convidados:
    print(nome_a_ser_buscado, 'seu nome está na lista! Boa festa!')
else:
    print('Infelizmente, você nâo foi convidado!')