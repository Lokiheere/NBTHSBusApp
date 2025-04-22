import os

from functools import wraps
from flask import jsonify, redirect, render_template, session, url_for, request
from app import socketio
from . import manage 
from . import management_bp

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

def login_required(f):
    @wraps(f)
    def access_control(*args, **kwargs):
        if 'loggedin' not in session:
            return redirect(url_for('authen.auth'))
        if kwargs.get('username') and session.get('name') != kwargs.get('username'):
            return redirect(url_for('authen.auth'))
        return f(*args, **kwargs)
    return access_control

@management_bp.route('/management/<username>', methods=['GET', 'POST'])
@login_required
def management(username):
    if 'loggedin' not in session:
        return redirect(url_for('authen.auth'))
    
    available_options, parking_spots = manage.get_available_data()

    msg = ''
    if request.method == 'POST':
        selected_bus = request.form.get('bus_selector')
        selected_spot = request.form.get('spot_selector')
        
        if not selected_bus or not selected_spot:
            msg = "Please select both a bus and a parking spot."
        else:
            msg = manage.process_selection(selected_bus, selected_spot)
            socketio.emit('new_assignment', {
                "bus": selected_bus,
                "spot": selected_spot,
                "message": msg
            })
            
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return jsonify({"message": msg})
            
            return redirect(url_for('management_bp.management', username=username))

        msg = manage.process_selection(selected_bus, selected_spot)

    print(f"Current options passed to template: {available_options}, Parking spots: {parking_spots}")
    
    return render_template('management/index.html', username=username, options=available_options, spots=parking_spots, msg=msg)

