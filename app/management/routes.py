from functools import wraps
from flask import redirect, render_template, session, url_for, request, jsonify

from . import manage
from . import management_bp

from app.utils import create_map


def login_required(f):
    @wraps(f)
    def access_control(*args, **kwargs):
        if 'loggedin' not in session:
            return redirect(url_for('authen.auth'))
        if kwargs.get('username') and session.get('name') != kwargs.get('username'):
            return redirect(url_for('authen.auth'))
        return f(*args, **kwargs)

    return access_control


@management_bp.route('/management/api/undo_assignments', methods=['POST'])
def undo_assignments():
    data = request.get_json()
    bus_name = data.get('bus_name')
    spot_name = data.get('spot_name')

    return manage.undo_selection(bus_name, spot_name)


@management_bp.route('/management/api/assignments')
def get_assignments():
    assigned_data = create_map.bus_setup()

    return jsonify(assigned_data)


@management_bp.route('/management/<username>', methods=['GET', 'POST'])
@login_required
def management(username):
    if 'loggedin' not in session:
        return redirect(url_for('authen.auth'))

    available_options, parking_spots = manage.get_available_data()

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

    return render_template('management/index.html', username=username, options=available_options, spots=parking_spots,
                           msg=msg)
