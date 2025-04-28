from flask import Flask, render_template
import stripe
import os
import json

app = Flask(__name__)
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

with open('app/products.json') as f:
    products = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

if __name__ == '__main__':
    app.run(debug=True)
