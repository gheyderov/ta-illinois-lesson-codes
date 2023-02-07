from flask import Flask, render_template

app = Flask(__name__)

products = {
    1 : {
        'id' : 1,
        'name' : 'Product #1',
        'description' : 'some description',
        'price' : 100,
        'image' : 'p1.avif'
    },
    2 : {
        'id' : 2,
        'name' : 'Product #2',
        'description' : 'some description',
        'price' : 200,
        'image' : 'p2.avif'
    },
    3 : {
        'id' : 3,
        'name' : 'Product #3',
        'description' : 'some description',
        'price' : 300,
        'image' : 'p3.avif'
    }
}

colors = ['red', 'blue', 'green']

@app.route("/home")
def home():
    return render_template('index.html', products = products)


@app.route("/product/<int:id>")
def product(id):
    return render_template('product.html', product = products[id], colors = colors)