from flask import Flask, render_template, request, redirect, url_for
import stripe
import os
import json
from stratosync_engine import StratoSyncEngine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Stripe API keys
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
YOUR_DOMAIN = 'https://trendforge-ai-v2.onrender.com'  # Change if your Render domain changes!

# Load products from JSON
with open('app/products.json') as f:
    products = json.load(f)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Products listing
@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

# Buy Now (create Stripe checkout session)
@app.route('/buy/<product_id>')
def buy(product_id):
    # Find the product by ID
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product['name'],
                    'description': product['description'],
                },
                'unit_amount': product['price_cents'],
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + '/thank-you',
        cancel_url=YOUR_DOMAIN + '/',
    )
    return redirect(checkout_session.url, code=303)

# Contact form submission (basic handling for now)
@app.route('/thank-you', methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you could use your Stratosync system to handle emails
        # (optional future expansion)
        print(f"Message from {name} ({email}): {message}")
    return render_template('thank-you.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
