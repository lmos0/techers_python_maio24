#Escreva uma função chamada inverter_string que receba uma string e retorne a string invertida.

def inverter_string(texto):
   return texto[::-1]

# print(inverter_string('banana'))

textinho = input('Digite a palavra a ser invertida! ')

print(inverter_string(textinho))