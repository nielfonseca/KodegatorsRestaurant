import banco_dados
import sqlite3
from flask import Flask, render_template, redirect, request

banco = bancod('registros.sqlite')
banco.criarTabelacliente()
banco.criarTabelaitem()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'KODEGATOR'

@app.route('/')
def home():
    
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    
    if login == 'daniel' and password == 'lucasgay123':
        return render_template("menu.html")
    
    return redirect('/')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    while True:
        login = request.form.get('login')
        password = request.form.get('password')
        new_password = request.form.get('new-password')
        if password == new_password:
            banco.inserir(login, password)
            False
            return render_template("login.html")
        else:
            True           



if __name__ in "__main__":
    app.run(debug=True)