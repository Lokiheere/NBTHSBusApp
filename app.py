"""
Flask Application Documentation

This Flask application handles user authentication and renders templates for the root, home, and authentication routes.

Routes:
1. `/` (Root Route):
   - Renders the main layout template.
   - Returns: Rendered HTML template for the layout page.

2. `/auth` (Authentication Route):
   - Handles user login for both GET and POST requests.
   - Delegates login logic to `admin_data_handler.login_user()`.
   - Returns: Response from `admin_data_handler.login_user()`, which could be a redirect or a rendered template.

3. `/logout` (Logout Route):
   - Handles user logout.
   - Delegates logout logic to `admin_data_handler.logout_user()`.
   - Returns: Response from `admin_data_handler.logout_user()`, typically a redirect to another page.

4. `/home` (Home Route):
   - Renders the home page for authenticated users.
   - Passes the username stored in the session to the template for personalized rendering.
   - Returns: Rendered HTML template for the home page, with the username passed as a context variable.
   - Raises: KeyError if the 'name' key is not found in the session, indicating the user is not logged in.
"""

from flask import Flask, render_template, session
from .auth import admin_data_handler
import os
from dotenv import load_dotenv 

app = Flask(__name__)

load_dotenv('.env')

app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def hello_world():
    return render_template('layout.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    return admin_data_handler.login_user()

@app.route('/logout')
def logout():
    return admin_data_handler.logout_user()

@app.route('/home')
def home():
    return render_template('home/index.html', username = session['name'])   