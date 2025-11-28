from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "mobilecharger-secret-key"

products = [
    {"id": 1, "name": "Fast Charger 20W", "price": 699},
    {"id": 2, "name": "USB-C Charger 18W", "price": 549},
    {"id": 3, "name": "Wireless Charger", "price": 1199}
]

def init_cart():
    if 'cart' not in session:
        session['cart'] = []

@app.route('/')
def index():
    init_cart()
    return render_template('index.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    for p in products:
        if p['id'] == id:
            return render_template('product.html', product=p)
    return redirect('/')

@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    init_cart()
    session['cart'].append(id)
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    init_cart()
    cart_items = [p for p in products if p['id'] in session['cart']]
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', items=cart_items, total=total)

@app.route('/checkout')
def checkout():
    session.clear()
    return "<h2>Order placed successfully! Thank you ❤️</h2>"

if __name__ == "__main__":
    app.run(debug=True)
