from flask import render_template, jsonify
from marshmallow import Schema, fields

class AssignmentSchema(Schema):
    bus_name = fields.String(required=True)
    spot_name = fields.String(required=True)

assignment_schema = AssignmentSchema(many=True)

from . import home_bp
from app.utils.create_map import bus_setup

@home_bp.route('/api/assignments')
def get_assignments():
    assigned_data = bus_setup()
    return jsonify(assignment_schema.dump(assigned_data))

@home_bp.route('/home')
def home():
    return render_template('home/index.html')

@home_bp.route('/form')
def form():
    return render_template('form/index.html')