from flask_app import app
from flask import render_template,redirect,request,session,flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')