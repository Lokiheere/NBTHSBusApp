from flask import Blueprint, redirect, render_template, session, url_for

management_bp = Blueprint('management_bp', __name__)

@management_bp.route('/management/<username>')
def management(username):
    return render_template('management/index.html', username=username)   

@management_bp.before_request
def restrict_access():
    if 'loggedin' not in session:
        return redirect(url_for('authen.auth'))