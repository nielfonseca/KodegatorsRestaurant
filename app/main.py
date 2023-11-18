

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KODEGATOR'

@app.route('/')
def home():
    
    return render_template('login.html')



@app.route('/menu', methods=['post'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    print(login)
    print(password)
    return redirect('/')










if __name__ in "__main__":
    app.run(debug=True)