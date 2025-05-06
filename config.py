import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False

    @staticmethod
    def init_app(app):
        app.config["DEBUG"] = True
        app.config["SESSION_COOKIE_HTTPONLY"] = True
        app.config["SESSION_COOKIE_SECURE"] = True


class DevelopmentConfig(Config):
    DEBUG = True
    autocommit = True
    reconnect = True
    DB_CONFIG = {
        'host': os.getenv('APP_HOST'),
        'user': os.getenv('APP_USER'),
        'password': os.getenv('APP_PASSWORD'),
        'database': os.getenv('APP_DATABASE'),
        'port': os.getenv('APP_PORT'),
    }


class ProductionConfig(Config):
    DEBUG = False
    autocommit = True
    reconnect = True
    DB_CONFIG = {
        "host": "placeholder_host",
        "user": "placeholder_user",
        "password": "placeholder_password",
        "database": "placeholder_db",
        "port": 3306,
    }
