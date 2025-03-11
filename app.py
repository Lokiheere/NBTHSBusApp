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

from flask import Flask, render_template
from home import routes as home_routes
from auth import routes as auth_routes
from errors import error_handlers
import os
from dotenv import load_dotenv 

app = Flask(__name__)

load_dotenv('.env')

app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def layout():
    return render_template('layout.html')

app.register_blueprint(error_handlers.error)

app.register_blueprint(auth_routes.authen)

app.register_blueprint(home_routes.home_bp)

if __name__ == '__main__':
    app.run(debug=True)