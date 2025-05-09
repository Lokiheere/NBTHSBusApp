from config import DevelopmentConfig, ProductionConfig
from flask import Flask, render_template, request
import os

from flask_limiter import Limiter

limiter = Limiter(key_func=lambda: request.remote_addr)

from flask_socketio import SocketIO

socketio = SocketIO()

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()


def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")

    config_class = ProductionConfig if env == "production" else DevelopmentConfig
    app.config.from_object(config_class)

    config_class.init_app(app)
    limiter.init_app(app)
    socketio.init_app(app)
    csrf.init_app(app)
    marshmallow.init_app(app)

    from app.errors import error_handlers
    app.register_blueprint(error_handlers.errors)

    from app.management import routes as management_routes
    app.register_blueprint(management_routes.management_bp)

    from app.auth import routes as auth_routes
    app.register_blueprint(auth_routes.authen)

    from app.home import routes as home_routes
    app.register_blueprint(home_routes.home_bp)

    @app.route('/')
    def main():
        return render_template('main/index.html')

    return app
