import tkinter

window = tkinter.Tk() #Instanciando um objeto do tipo Janela Tkinter 

window.title('Tela de Login')
window.geometry('340x440')

def hello_world():
    print('Hello World!')

#Instaciamento dos objetos na tela usando o método grid
label = tkinter.Label(window, text='Imprima Hello World no terminal', font=('Arial, 12'))
entry = tkinter.Entry(window)
button = tkinter.Button(window, text='Clique Aqui!', bg='blue', fg='white', font=('Arial', 12), command=hello_world ) # Passo 1: Criação do Widget
button2 = tkinter.Button(window, text='Dúvidas?', bg='red', fg='white')


#Posicionamento dos widgets da tela, utilizando o método grid


label.grid(row=0, column= 1)
entry.grid(row=2, column=1)
button.grid(row=1, column=1)
button2.grid(row=3, column=1)


window.mainloop() # Mantendo a janela aberta para execução do programa

