class Mamifero:
    def __init__ (self, nome ):
        self.nome = nome
    
    def fazer_som(self):
        pass

    def mover(self):
        print(f'{self.nome} está se movendo')

    def mamar(self):
        print(f'{self.nome} está mamando')

class Cachorro(Mamifero):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca 

    def fazer_som(self):
        print(f'{self.nome}, da raça {self.raca} está latindo: au au')

    def corrr_atras_do_rabo(self):
        print(f'{self.nome} está correndo atrás do próprio rabo')
        

pacoca = Cachorro("Paçoquinha", "Vira-lata")
mel = Cachorro('Mel', 'Poodle')

pacoca.mamar()

morcego = Mamifero("Batman")

morcego.mamar()
morcego.mover()

mel.fazer_som()
mel.corrr_atras_do_rabo()

morcego.corr