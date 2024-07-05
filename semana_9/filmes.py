import tkinter, requests 

root = tkinter.Tk()

root.title('Informações sobre filmes')
root.geometry('450x325')
#root.configure(background='gray')

root.resizable(False,False)

chave = '35d90404'

def movie(filme_consultado):

    url = f'https://www.omdbapi.com/?t={filme_consultado}&apikey=35d90404'
    resposta = requests.get(url)
    data = resposta.json()

    if data['Response'] == "True":
        filme = data

        info = (f'O filme consultado é {filme['Title']}\n'
        f'O ano de lançamento do filme foi {filme['Year']}\n'
        f'A nota no IMDB é de {filme['imdbRating']}\n'
        f'A direção do filme é feito por {filme['Director']}\n'
        f'O elenco é composto por {filme['Actors']}\n'
        f'País do filme: {filme['Country']}')

        return info

    else:
        return 'Filme não encontrado ou falha na API'


def update_label():
    user_choice = entry.get()
    text = movie(user_choice)
    label.config(text=text)

#Criação Widgets

frame = tkinter.Frame()
button = tkinter.Button(frame, text='Clique aqui', command=update_label)
entry = tkinter.Entry(frame,)
label = tkinter.Label(frame, text='As informações do filme aparecerão aqui!', font=('Roboto', 10))



#Posicionamento Wdigets

frame.pack(pady='10')

entry.pack(pady='5')
button.pack(pady='10')
label.pack(pady='5')
root.mainloop()