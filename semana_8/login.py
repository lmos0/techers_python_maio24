import tkinter 

window = tkinter.Tk()

window.title('Tela de Login')
window.geometry('340x440')


#Criar os widgets

login_label = tkinter.Label(window, text='Login', font=('Arial', 14))
email_label = tkinter.Label(window, text = 'E-mail cadastrado', bg='blue')
password_label = tkinter.Label(window, text='Senha', bg='#DF3737')

email_entry = tkinter.Entry(window)
password_entry = tkinter.Entry(window, show='*')

login_button = tkinter.Button(window, text='Logar')

#Posicionar elementos

login_label.grid(row=0, column=0, columnspan=2)
email_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)

email_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

login_button.grid(row=3, column=0, columnspan=3)

# login_label.pack()
# email_label.pack()
# password_label.pack()

# email_entry.pack()
# password_entry.pack()

# login_button.pack()


window.mainloop()