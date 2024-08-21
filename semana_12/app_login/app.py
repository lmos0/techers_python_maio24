from flask import Flask, request, render_template, url_for, redirect, flash, session 

app = Flask(__name__)

app.secret_key = '5c1998b478720a9c5f65c3a3b2a142a1'# Necessário pra usarmos os métodos session e flash em segurança

#Dicionário para armazenar as credenciais do usuário. Pseudo banco de dados
usuarios = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('senha')

        if not username or not senha:
            flash('Username e senha são obrigatórios', 'error')
        elif username in usuarios:
            flash('Usuário já cadastrado', 'error')
        else:
            usuarios[username] = senha
            flash('Usuário cadastrado com sucesso', 'success')
            print(usuarios)
            return redirect (url_for('login'))

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('senha')

    if not username or not senha:
        flash('Username e senha são obrigatórios', 'error')
    elif username not in usuarios or usuarios[username] != senha:
        flash('Credenciais inválidas', 'error')
    else:
        session['username'] = username
        flash('Login realizado com sucesso', 'success')
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)