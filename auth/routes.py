from flask import Blueprint
from . import admin_data_handler

authen = Blueprint('authen', __name__)

@authen.route('/auth', methods=['GET', 'POST'])
def auth():
    return admin_data_handler.login_user()

@authen.route('/logout')
def logout():
    return admin_data_handler.logout_user()