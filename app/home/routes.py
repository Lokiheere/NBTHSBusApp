from flask import render_template
from . import home_bp

@home_bp.route('/home')
def home():
    return render_template('home/index.html')    

@home_bp.route('/form')
def form():
    return render_template('form/index.html')