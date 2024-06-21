class Cachorro:
    def __init__(self, nome, raca, peso): #Atributos necessários para iniciar um objeto do tipo Cachorro
        self.nome = nome
        self.raca = raca 
        self.peso = peso
    
    def latir(self): #Criando o método (função que executa uma ação do meu objeto) latir 
        print(f'{self.nome} diz Au au')

    def dar_alta(self):
        print('Paciente liberado')

cachorro1 = Cachorro('Paçoca', 'Vira-lata', '4kg') #cachorro1 é uma instância(um objeto) da classe Cachorro(que é um tipo de dado específico)
cachorro2 = Cachorro('Batatinha', 'Pug', '2kg') 

cachorro1.latir() #.latir() é método inerente à classe Cachorro. E todas instâncias/objetos dessa classe, podem executá-lo
cachorro2.latir()