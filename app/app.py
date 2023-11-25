from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os, json
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KODEGATOR'

UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

foods = []
drinks = []

on = False

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    global on
    on = False
    
    return render_template('login.html')



@app.route('/cadastros')
def cadastros():

    return render_template('cadastro.html')

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

    newlogin = usuarios + user

    with open('usuarios.json', 'w') as gravarTemp:
        json.dump(newlogin, gravarTemp, indent=4)

    return redirect('/')

@app.route('/cardapio', methods=['POST'])
def login():

    global on

    login = request.form.get('login')
    password = request.form.get('password')

    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)
        cont = 0

        for usuario in usuarios:
            cont += 1
            if login == 'admin' and password == 'admin123':
                on = True
                return redirect('/admin')
                
            if usuario['login'] == login and usuario['password'] == password:
                return render_template('menu.html', foods=foods, drinks=drinks)
            if cont >= len(usuarios):
                flash('USUARIO E SENHA INVALIDOS')
                return redirect('/')
            

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    
    global foods, drinks

    if on == True:
        if request.method == 'POST':
            for food in foods:
                food['price'] = request.form.get(f'food_{food["item"]}_price', food['price'])
            for drink in drinks:
                drink['price'] = request.form.get(f'drink_{drink["item"]}_price', drink['price'])
        return render_template('menu_admin.html', foods=foods, drinks=drinks)
    if on == False:
        return redirect('/')


@app.route('/add_item', methods=['POST'])
def add_item():
    global foods, drinks
    item = request.form['item']
    description = request.form['description']
    category = request.form['category']
    image = request.files['image']
    price = request.form['price']

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        # Redimensionar a imagem para 120x120 pixels
        resized_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resized_' + filename)
        with Image.open(image_path) as img:
            img.thumbnail((120, 120))
            img.save(resized_image_path)

        # Salvar o nome do arquivo e o preço na lista
        if category == 'food':
            foods.append({'item': item, 'description': description, 'image': 'resized_' + filename, 'price': price})
        elif category == 'drink':
            drinks.append({'item': item, 'description': description, 'image': 'resized_' + filename, 'price': price})

    return redirect(url_for('admin'))

@app.route('/remove_item', methods=['POST'])
def remove_item():
    global foods, drinks
    item = request.form['item']
    category = request.form['category']

    if category == 'food' and item in [food['item'] for food in foods]:
        removed_item = [food for food in foods if food['item'] == item][0]
        foods = [food for food in foods if food['item'] != item]
    elif category == 'drink' and item in [drink['item'] for drink in drinks]:
        removed_item = [drink for drink in drinks if drink['item'] == item][0]
        drinks = [drink for drink in drinks if drink['item'] != item]

    # Remover a imagem associada ao item
    if 'image' in removed_item:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resized_' + removed_item['image'])
        if os.path.exists(image_path):
            os.remove(image_path)

    return redirect(url_for('admin'))

@app.route('/kodegator')
def kodegator():
    
    return render_template('kodegator.html')

@app.route('/contato')
def contatos():

    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)