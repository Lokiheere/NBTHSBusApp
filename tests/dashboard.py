from flask_admin import expose, BaseView
from dotenv import load_dotenv
import os
from app.utils.db_connect import get_connection

load_dotenv(".env")

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

connection = get_connection(host, user, password, database, port)

cursor = connection.cursor(dictionary=True)

class UserView(BaseView):
    @expose('/')
    def index(self):
        cursor.execute("SELECT name FROM users")
        users = cursor.fetchall()  
        return self.render('admin/users.html', users=users)