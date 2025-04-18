from flask import redirect, session, url_for
from . import authen
from . import admin_data_handler

@authen.route('/auth', methods=['GET', 'POST'])
def auth():
    if 'loggedin' in session:
        username = session.get('name')
        return redirect(url_for('management_bp.management', username=username))
    return admin_data_handler.login_user()

@authen.route('/logout')
def logout():
    return admin_data_handler.logout_user()