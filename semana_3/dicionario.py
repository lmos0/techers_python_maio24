 
#Dicionãrio é uma estrutura de dados que permite associar um valor com outro 

#Chave e valor 

dicionario_de_emails = {
    'Luís': 'luis@gmail.com',
    'Lucas': 'lucas@outlook.com',
    'Marcela': 'marcela@hotmail.com',
    'Luís': 'luism@yahoo.com'
}

for nome in dicionario_de_emails:
    print(nome) # Essa estrutura imprime cada chave dentro do dicionário, e NÃO retorna o valor correspondente (ou seja o e-mail)

for email in dicionario_de_emails:
    print(dicionario_de_emails[email]) # Essa estrutura o loop acessará o valor de cada chave dentro do dicionário