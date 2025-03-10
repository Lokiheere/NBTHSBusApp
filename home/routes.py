from flask import Blueprint, redirect, render_template, session, url_for

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/home')
def home():
    return render_template('home/index.html', username = session['name'])   

@home_bp.before_request
def restrict_access():
    if 'loggedin' not in session:
        return redirect(url_for('authen.auth'))