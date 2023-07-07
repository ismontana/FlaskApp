from flask import (Flask, render_template, request, redirect, url_for, flash )
from db.categories import Category 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/saludo/<name>")
def saludo(name):
    user = 'admin'
    return render_template('saludo.html', name=name, user=user)

@app.route("/drinks")
def drinks():
    drinks = ["agua", "jugo", "limonada", "coca", "sprite"]
    return render_template('drinks.html', drinks=drinks)

@app.route('/categories/')
def categories():
    cats = Category.get_all()
    return render_template('categories.html', cats=cats)

@app.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    if request.method == 'POST':
        #Guardar
        category = request.form['category']
        description = request.form['description']
        if not category:
            flash('Debes ingresar una categoría')
        elif not description:
            flash('Debes ingresar una descripción')
        else:
            cat = Category(category, description)
            cat.save()
        return redirect(url_for('categories'))
    return render_template('create_cat.html')

@app.route('/categories/<int:id>/update/')
def update_cat(id):
    return f"Vamos a editar con id { id }"

@app.route('/categories/<int:id>/delete/')
def delete_cat(id):
    cat = Category.get(id)
    cat.delete()
    return redirect(url_for('categories'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)