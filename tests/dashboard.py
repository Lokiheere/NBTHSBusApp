from flask_admin import expose, BaseView
from dotenv import load_dotenv
import os
from app.utils.db_connect import DBConnection

load_dotenv(".env")

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

class UserView(BaseView):
    @expose('/')
    def index(self):
        with DBConnection(host, user, password, database, port) as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        return self.render('admin/users.html', users=users)
    
