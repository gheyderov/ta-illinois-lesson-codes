from app import app
from flask import render_template, request
from models import Product, Contact, Category
from forms import ContactForm




@app.route("/home")
def home():
    items = Product.query.all()
    categories = Category.query.all()
    return render_template('index.html', products = items, categories = categories)


@app.route("/category/<string:name>")
def cat(name):
    items = Category.query.filter_by(name = name).first().product
    categories = Category.query.all()
    return render_template('index.html', products = items, categories = categories)




@app.route("/product/<int:id>")
def product(id):
    item = Product.query.filter_by(id = id).first()
    return render_template('product.html', product = item)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.form)
        if form.validate_on_submit():
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                company = form.company.data,
                message = form.message.data,
                is_subscribe = form.is_subscribe.data
            )
            contact.save()
    return render_template('contact.html', form = form)