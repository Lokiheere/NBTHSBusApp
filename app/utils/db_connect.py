import os
import mysql.connector
from config import DevelopmentConfig, ProductionConfig

def get_db_config():
    env = os.getenv("FLASK_ENV", "development")
    return ProductionConfig.DB_CONFIG if env == "production" else DevelopmentConfig.DB_CONFIG

def get_connection(): 
    db_config = get_db_config()
    return mysql.connector.connect(**db_config)

