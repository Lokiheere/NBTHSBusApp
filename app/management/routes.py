from functools import wraps
from flask import redirect, render_template, session, url_for
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

@management_bp.route('/management/<username>')
@login_required
def management(username):
    if 'loggedin' not in session:
        return redirect(url_for('authen.auth'))
    return render_template('management/index.html', username=username)   
    
# @management_bp.route('/admin/')
# @login_required
# def admin():
#     if 'loggedin' not in session:
#         return redirect(url_for('authen.auth'))
#     return render_template('admin/index.html')