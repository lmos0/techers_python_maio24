#Crie um sistema simples de gerenciamento de uma biblioteca que permite adicionar, remover e consultar livros.

# **Defina a Classe `Livro`**:

# - A classe deve ter os seguintes atributos:
#     - `titulo`: o título do livro (tipo: `str`)
#     - `autor`: o autor do livro (tipo: `str`)
#     - `ano_publicacao`: o ano de publicação do livro (tipo: `int`)

class Livro:
    def __init__(self, titulo:str, autor:str, ano_publicacao:int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def __str__(self):
        return f' \t{self.titulo} \t{self.autor} \t{self.ano_publicacao}'


class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro:Livro):
        self.livros.append(livro)
        print(f'O livro {livro.titulo} foi adicionada à biblioteca')
    
    def remover_livro(self, titulo:str):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print('Livro {titulo} foi removido da biblioteca')
                return 
        print(f'O livro {titulo} não foi encontrado na biblioteca')

    def consultar_livro(self):
        if not self.livros: 
            print("Não há livros na biblioteca")
        else:
            print('Atualmente há o seguintes livros na biblioteca:')
            for livro in self.livros:
                print(f' - {livro}')


livro1 = Livro("Python para Iniciantes", "Lucas Matheus", 2025)
livro2 = Livro('Vidas Secas', 'Gracilianos Ramos', 1938 )
livro3 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881)

biblioteca = Biblioteca()


print(livro1)
biblioteca.consultar_livro()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.consultar_livro()