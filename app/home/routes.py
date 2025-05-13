from flask import render_template, jsonify

from . import home_bp
from app.utils.create_map import bus_setup

@home_bp.route('/home/api/assignments')
def get_assignments():
    assigned_data = bus_setup()
    return jsonify(assigned_data)

@home_bp.route('/home')
def home():
    return render_template('home/index.html')

@home_bp.route('/form')
def form():
    return render_template('form/index.html')