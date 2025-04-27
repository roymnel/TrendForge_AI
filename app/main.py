from flask import Flask, render_template, request, redirect, url_for
import stripe
import os
import json

app = Flask(__name__)

# Stripe setup
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Load products
with open('app/products.json') as f:
    products = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', products=products)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

@app.route('/create-checkout-session/<product_id>', methods=['POST'])
def create_checkout_session(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if not product:
        return redirect(url_for('portfolio'))
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product['name'],
                },
                'unit_amount': product['price_cents'],
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('thank_you', _external=True),
        cancel_url=url_for('portfolio', _external=True),
    )
    return redirect(session.url, code=303)

if __name__ == '__main__':
    app.run(debug=True)
