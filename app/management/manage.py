from flask_admin import Admin
from dotenv import load_dotenv
import os
from utils.db_connect import get_connection

load_dotenv(".env")

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

connection = get_connection(host, user, password, database, port)

cursor = connection.cursor()
