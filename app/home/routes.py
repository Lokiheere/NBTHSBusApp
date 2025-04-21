from flask import render_template
from . import home_bp

@home_bp.route('/home')
def home():
    return render_template('home/index.html')    

    