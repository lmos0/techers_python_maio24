import tkinter
from tkinter import ttk


def retrieve():

    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationalty_combobox.get()

    status = reg_status_var.get()
    terms = terms_check_var.get()

    disciplines = disciplines_spinbox.get()

    print('Nome:', firstname)
    print('Sobrenome', lastname)
    print('Titulação Máxima', title)
    print('Idade', age)
    print('Nacionalidade', nationality)
    print('Status Acadêmico', status)
    print('Termos e Condições', terms)
    print('Número de disciplinas cursadas', disciplines)




root = tkinter.Tk()
root.title('Cadastro Acadêmico')

#Widgets primários
frame = tkinter.Frame(root)
user_info_frame = tkinter.LabelFrame(frame, text='Informações do Usuário')


#Criação de widgets
first_name_label = tkinter.Label(user_info_frame, text='Nome')
last_name_label = tkinter.Label(user_info_frame, text='Sobrenome')

pronome_label = tkinter.Label(user_info_frame, text='Pronome de Preferência')
pronome_combobox = ttk.Combobox(user_info_frame, values=['Prefiro não informar', 'Senhor', 'Senhora', 'Outro'])

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)

title_label = tkinter.Label(user_info_frame, text='Titulação Máxima')
title_combobox = ttk.Combobox(user_info_frame, values=['', 'Bacharelado', 'Mestrado', 'Douturado'])

age_label = tkinter.Label(user_info_frame, text='Idade')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=16, to=110)


nationality_label = tkinter.Label(user_info_frame, text='Nacionalidade')
nationalty_combobox = ttk.Combobox(user_info_frame, values=["Afeganistão", "Albânia", "Argélia", "Andorra", "Angola", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bielorrússia", "Bélgica", "Belize", "Benin", "Butão", "Bolívia", "Bósnia e Herzegovina", "Botswana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", "Camboja", "Camarões", "Canadá", "Cabo Verde", "Chade", "Chile", "China", "Colômbia", "Comores", "Congo", "Costa Rica", "Croácia", "Cuba", "Chipre", "República Checa", "Dinamarca", "Djibouti", "Dominica", "República Dominicana", "Timor Leste", "Equador", "Egito", "El Salvador", "Guiné Equatorial", "Eritreia", "Estônia", "Eswatini", "Etiópia", "Fiji", "Finlândia", "França", "Gabão", "Gâmbia", "Geórgia", "Alemanha", "Gana", "Grécia", "Granada", "Guatemala", "Guiné", "Guiné-Bissau", "Guiana", "Haiti", "Honduras", "Hungria", "Islândia", "Índia", "Indonésia", "Irã", "Iraque", "Irlanda", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Cazaquistão", "Quênia", "Kiribati", "Coreia do Norte", "Coreia do Sul", "Kuwait", "Quirguistão", "Laos", "Letônia", "Líbano", "Lesoto", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Madagascar", "Malawi", "Malásia", "Maldivas", "Mali", "Malta", "Ilhas Marshall", "Mauritânia", "Maurício", "México", "Micronésia", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Marrocos", "Moçambique", "Myanmar", "Namíbia", "Nauru", "Nepal", "Países Baixos", "Nova Zelândia", "Nicarágua", "Níger", "Nigéria", "Macedônia do Norte", "Noruega", "Omã", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", "Paraguai", "Peru", "Filipinas", "Polônia", "Portugal", "Catar", "Romênia", "Rússia", "Ruanda", "Samoa", "San Marino", "São Tomé e Príncipe", "Arábia Saudita", "Senegal", "Sérvia", "Seychelles", "Serra Leoa", "Cingapura", "Eslováquia", "Eslovênia", "Ilhas Salomão", "Somália", "África do Sul", "Espanha", "Sri Lanka", "Sudão", "Sudão do Sul", "Suriname", "Suécia", "Suíça", "Síria", "Taiwan", "Tajiquistão", "Tanzânia", "Tailândia", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turquia", "Turcomenistão", "Tuvalu", "Uganda", "Ucrânia", "Emirados Árabes Unidos", "Reino Unido", "Estados Unidos", "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Iêmen", "Zâmbia", "Zimbábue"])


#posicionamento
frame.pack()
user_info_frame.grid(row=0, column=0, padx=20, pady=20) #20px de distância da borda horizontal (padx) e 20px de distância da borda vertical (pady)

first_name_label.grid(row=0, column=1)
last_name_label.grid(row=0, column=2)

first_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1,column=2)

title_label.grid(row=2, column=2)
title_combobox.grid(row=3, column=2)

age_label.grid(row=2, column=0)
age_spinbox.grid(row=3,column=0)

nationality_label.grid(row=2, column=1)
nationalty_combobox.grid(row=3, column=1)

pronome_label.grid(row=0, column=0)
pronome_combobox.grid(row=1, column=0)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=3)
    #Loop para mudar a configuração de paddings do widgets filhos da objeto user_info_frame

###Segundo Frame

courses_frame = tkinter.LabelFrame(frame)
status_label = tkinter.Label(courses_frame, text='Status Acadêmico')

reg_status_var = tkinter.StringVar(value='Não')
registred_check = tkinter.Checkbutton(courses_frame, text='Regularmente Matriculado', onvalue='Sim', offvalue='Não')

disciplines_label = tkinter.Label(courses_frame, text="Número de Matérias Matriculadas")
disciplines_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='10')





courses_frame.grid(row=1, column=0, padx=20, pady=20)
status_label.grid(row=0,column=0)

registred_check.grid(row=1, column=0)

disciplines_label.grid(row=0, column=1)
disciplines_spinbox.grid(row=1,column=1)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=3)

### frame 3

terms_frame = tkinter.LabelFrame(frame, text='Termos e Condições')
terms_check_var = tkinter.StringVar(value='Não Concorda')
terms_check = tkinter.Checkbutton(terms_frame, text='Eu aceito os termos e condições', variable=terms_check_var, onvalue='Concorda', offvalue='Não Concorda')

button = tkinter.Button(frame, text='Enviar', command=retrieve)


#posicionamento

terms_frame.grid(row=2, column=0, padx=20, pady=20)
terms_check.grid(row=0,column=0)

button.grid(row=3, column=0, pady=5)


root.mainloop()