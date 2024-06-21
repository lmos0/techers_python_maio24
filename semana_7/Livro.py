class Livro:
    def __init__(self, titulo, autor, editora, numero_paginas, em_estoque=True): #Método construtor para definir os atributos (características) necessárias para instanciamento (criação) do objeto
        self.titulo = titulo #Recebe os valores informados no momento da criação do objeto e guardar na variável do respectivo objetivo (self.algumacoisa)
        self.autor = autor
        self.editora = editora
        self.numero_paginas = numero_paginas
        self.em_estoque = em_estoque

    def resumir(self):
        print(f'Título: {self.titulo}')   
        print(f'Autor: {self.autor}' )
        print(f'Editora: {self.editora}')
        print(f'Número de Páginas: {self.numero_paginas}')

    def vender(self):
        print('O livro foi vendido')
        self.em_estoque = False

livro0 = Livro('A Revolução dos Bichos', 'George Orwell', 'Companhia das Letras', 128)
livro1 = Livro('O Senhor dos Aneis: A Sociedade do Anel', 'Tolkien', 'Martins Fontes', 504)

print(livro0.em_estoque)

livro0.vender()
print(livro0.em_estoque)