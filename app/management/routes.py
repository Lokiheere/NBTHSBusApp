from functools import wraps
from flask import redirect, render_template, session, url_for, request

from . import manage
from . import management_bp

from app.utils.create_map import bus_setup

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

            session['msg'] = msg

            return redirect(url_for('management_bp.management', username=username))

        else:
            msg = manage.process_selection(selected_bus, selected_spot)
            
            session['msg'] = msg
            
            return redirect(url_for('management_bp.management', username=username))

    msg = session.pop('msg', '')

    print(f"Current options passed to template: {available_options}, Parking spots: {parking_spots}")

    assigned_data = bus_setup()


    return render_template('management/index.html', username=username, options=available_options, spots=parking_spots, msg=msg, assigned_data=assigned_data)

@management_bp.route('/management/<username>/undo_selection', methods=['POST'])
@login_required
def undo_selection(username):
    selected_bus_undo = request.form.get("bus_name")
    selected_spot_undo = request.form.get("spot_name")

    print(f"Receive Bus: {selected_bus_undo} Spot: {selected_spot_undo}")  # Debug Output

    if not selected_bus_undo or not selected_spot_undo:
        session["msg"] = "Invalid undo request."
    else:
        session["msg"] = manage.undo_selection(selected_bus_undo, selected_spot_undo)

    return management(username)
