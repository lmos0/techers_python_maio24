nome = int(input('Digite seu nome: '))
idade = input('Digite sua idade: ')
profissao = input('Digite sua profissão ')

'Isto é uma string, mas em Python chamamos de "str" '

int = 3
floats = 3.0

print('O nome do usuário é', nome, 'a idade do usuário é', idade, 'a profissão do usuário é', profissao)
print('O nome do usuário é ' +  nome +  'a idade do usuário é '+  idade+  ' a profissão do usuário é '+ profissao)
print(f'O nome do usuário é {nome}, a idade do usuário é {idade} e a profissão do usuário é {profissao}')

#interpolação de strings 