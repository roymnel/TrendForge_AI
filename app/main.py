from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Services Page
@app.route('/services')
def services():
    return render_template('service.html')

# Projects Page
@app.route('/projects')
def projects():
    return render_template('project.html')

# Blog Page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Team Page
@app.route('/team')
def team():
    return render_template('team.html')

# Testimonial Page
@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
