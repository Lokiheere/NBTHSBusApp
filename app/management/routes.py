from functools import wraps
from flask import redirect, render_template, session, url_for
from . import management_bp


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'loggedin' not in session or session.get('name') != kwargs.get('username'):
            return redirect(url_for('authen.auth'))
        return f(*args, **kwargs)
    return decorated_function

@management_bp.route('/management/<username>')
@login_required
def management(username):
    if 'loggedin' not in session:
        return redirect(url_for('authen.auth'))
    return render_template('management/index.html', username=username)   
    
@management_bp.before_request
def check_admin():
    if 'admin' in session:
        return redirect(url_for('management_bp.management', username=session['name']))

