# Se a nota for maior que 90, o aluno tirou A
# Acima 80 B
# Acima de 70 C
# Acima de 60 D
# Menos de 60 F 

nota = int(input('Digite a nota do aluno: '))

if nota >= 90:
    print('A')
elif nota >= 80:
    print('B')
elif nota >= 70:
    print('C')
elif nota >= 60:
    print('D')
elif nota < 60:
    print('F')

# Usamos o elif para encontrar a primeira condição que seja verdadeira e encerramos a checagem uma vez que ela foi encontrada