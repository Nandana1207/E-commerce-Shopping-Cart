from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2000},
]

cart = []

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add/<int:id>')
def add_to_cart(id):
    for product in products:
        if product['id'] == id:
            cart.append(product)
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

if __name__ == '__main__':
    app.run(debug=True)