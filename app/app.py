from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image

app = Flask(__name__)

# Configurações para o upload de arquivos
UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

foods = []
drinks = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('menu.html', foods=foods, drinks=drinks)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    
    global foods, drinks

    if request.method == 'POST':
        # Se um preço for submetido, atualiza os preços
        for food in foods:
            food['price'] = request.form.get(f'food_{food["item"]}_price', food['price'])
        for drink in drinks:
            drink['price'] = request.form.get(f'drink_{drink["item"]}_price', drink['price'])
    return render_template('menu_admin.html', foods=foods, drinks=drinks)


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


if __name__ == '__main__':
    app.run(debug=True)