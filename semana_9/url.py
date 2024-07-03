import tkinter, pyshorteners

root = tkinter.Tk()
root.title('Encurtador de URL - Techers')
root.geometry('350x150')


def encurtador():
    encurtador = pyshorteners.Shortener()
    url_encurtada = encurtador.tinyurl.short(url_insert.get())
    url_retrive.insert(0, url_encurtada)



url_label = tkinter.Label(root, text='Insira o URL a ser encurtado')
url_insert = tkinter.Entry(root)
url_label2 = tkinter.Label(root, text='Link encurtado')
url_retrive = tkinter.Entry(root)
url_button = tkinter.Button(root, text='Enviar', command=encurtador)

url_label.pack()
url_insert.pack()
url_label2.pack()
url_retrive.pack()
url_button.pack()

root.mainloop()