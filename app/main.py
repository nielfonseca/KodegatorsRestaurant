

from flask import Flask, render_template, redirect, request

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
    else:
        return redirect('/')










if __name__ in "__main__":
    app.run(debug=True)