
#Crie uma classe Aluno com os atributos:


# nome (string), 
# matricula (string), 
# curso (sting) e 
# notas (lista). 


# Implemente um método calcular_media() que retorna a média das notas do aluno.
#return 

class Aluno:
    def __init__(self,nome:str, matricula:str, curso:str, notas:list):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas)/len(self.notas)
        return media
    
aluno1 = Aluno('João Henrique', '123456', 'Ciências da Computação', [8,7,10,6,9])
aluno2 = Aluno('Eduarda', '987654', 'Relações Internacionais', [9,10,5,4,8])

print(aluno1.calcular_media())
print(aluno2.calcular_media())

lista_de_notas = []
nota_do_aluno = float(input('Digite a nota')  )
lista_de_notas.append(nota_do_aluno)     

aluno3 = Aluno('Zé', '334323', 'Direito', lista_de_notas )