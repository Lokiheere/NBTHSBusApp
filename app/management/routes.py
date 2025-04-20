from functools import wraps
from flask import redirect, render_template, session, url_for, request
from . import manage 
from . import management_bp

def login_required(f):
    @wraps(f)
    def access_control(*args, **kwargs):
        if 'loggedin' not in session:
            return redirect(url_for('authen.auth'))
        if kwargs.get('username') and session.get('name') != kwargs.get('username'):
            return redirect(url_for('authen.auth'))
        return f(*args, **kwargs)
    return access_control

from app.management.manage import available_options

@management_bp.route('/management/<username>', methods=['GET', 'POST'])
@login_required
def management(username):
    if 'loggedin' not in session:
        return redirect(url_for('authen.auth'))
    
    global available_options
    msg = ''

    print(f"Current options passed to template: {available_options}")

    if request.method == 'POST':
        selected_option = request.form.get('selector')
        available_options, msg = manage.process_selection(selected_option, available_options)
        print(f"Current options passed to template: {available_options}")
        
    print(f"Current options passed to template: {available_options}")

    return render_template('management/index.html', username=username, options=available_options, msg=msg)
