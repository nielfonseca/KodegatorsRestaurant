import json
from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KODEGATOR'

@app.route('/')
def home():
    
    return render_template('login.html')

@app.route('/adm')
def adm():

    return render_template('cadastro.html')

@app.route('/cardapio', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)
        cont = 0

        for usuario in usuarios:
            cont += 1
            if login == 'admin' and password == 'admin123':
                return redirect('/adm')

            if usuario['login'] == login and usuario['password'] == password:
                return render_template("menu.html")
            if cont >= len(usuarios):
                flash('USUARIO E SENHA INVALIDOS')
                return redirect('/')
            
            
@app.route('/cadastro', methods=['POST'])
def cadastro():
    user = []
    login = request.form.get('login')
    password = request.form.get('password')

    user= [
        {
            "login": login,
            "password": password
        }
    ]
    
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)

    newlogin = user + usuarios

    with open('usuarios.json', 'w') as gravarTemp:
        json.dump(newlogin, gravarTemp, indent=4)

    return redirect('/')

if __name__ in "__main__":
    app.run(debug=True)