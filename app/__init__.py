from flask import Flask, render_template, request
import os

from flask_limiter import Limiter
limiter = Limiter(key_func=lambda: request.remote_addr)

from flask_socketio import SocketIO
socketio = SocketIO()

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["DEBUG"] = True

    app.secret_key = os.getenv('SECRET_KEY')
    
    limiter.init_app(app)
    socketio.init_app(app)
    
    @app.route('/')
    def main():
        return render_template('main/index.html')

    from app.errors import error_handlers
    app.register_blueprint(error_handlers.error)

    from app.management import routes as management_routes
    app.register_blueprint(management_routes.management_bp)

    from app.auth import routes as auth_routes
    app.register_blueprint(auth_routes.authen)

    from app.home import routes as home_routes
    app.register_blueprint(home_routes.home_bp)
    
    return app