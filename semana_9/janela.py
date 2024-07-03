import tkinter as tk

janela = tk.Tk() # Criação da janela principal
janela.title('Exercício TECHERS')


#Criação do Widget
rotulo = tk.Label(janela, text='Hello World', font=('Arial', 12))
botao = tk.Button(janela, text='Clique aqui', font=('Arial', 14))
entrada = tk.Entry(janela, font=('Arial, 16'))


#Posicionamento do Widget
rotulo.pack()
botao.pack()
entrada.pack()

janela.mainloop()
