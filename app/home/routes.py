from flask import render_template

from . import home_bp
from app.utils.create_map import bus_setup

@home_bp.route('/home')
def home():
    assigned_data = bus_setup()
    return render_template('home/index.html', assigned_data=assigned_data)

@home_bp.route('/form')
def form():
    return render_template('form/index.html')