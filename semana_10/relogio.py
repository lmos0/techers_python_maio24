#Objetivo:  criar uma aplicação que exiba a data e a hora ao clicar em um botão.

import tkinter as tk
from datetime import datetime

def mostrar_data_hora():
    agora = datetime.now()
    data_hora_formatada = agora.strftime("%d/%m/%Y, %H:%M:%S")
    label.config(text=data_hora_formatada)
   

janela = tk.Tk()
janela.title('Exibir Data e Hora')
janela.geometry('350x200')


button = tk.Button(janela, text='Mostrar Data e Hora', command=mostrar_data_hora)
label = tk.Label(janela, text='')

button.pack()
label.pack()

janela.mainloop()