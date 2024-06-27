class Veiculo:
    def mover(self):
        pass 

class Carro(Veiculo):
    def mover(self):
        print( "O carro está se movendo sobre quatro rodas")

class Moto(Veiculo):
    def mover(self):
        print( 'A moto está se movendo sobre duas rodas')
    

moto1 = Moto()
carro1 = Carro()

moto1.mover() #Exemplo de polimorfismo sendo exeuctado
carro1.mover() #idem
