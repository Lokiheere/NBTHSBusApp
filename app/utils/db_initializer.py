import os
from app.utils.db_connect import get_connection

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

def initialize_database():
    connection = get_connection(host, user, password, database, port)
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS buses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            bus_name VARCHAR(255) NOT NULL UNIQUE,
            assigned_spot VARCHAR(255) DEFAULT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parking_spots (
            id INT AUTO_INCREMENT PRIMARY KEY,
            spot_name VARCHAR(255) NOT NULL UNIQUE,
            occupied_by VARCHAR(255) DEFAULT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            passcode VARCHAR(255) NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("Database initialized successfully.")