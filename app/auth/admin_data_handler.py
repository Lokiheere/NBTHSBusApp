from flask import render_template, request, session, redirect, url_for
from dotenv import load_dotenv
import os
from app.utils.db_connect import get_connection

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

connection = get_connection(host, user, password, database, port)

cursor = connection.cursor()

def login_user():
    msg = ''
    if request.method == 'POST':
        name = request.form['name']
        passcode = request.form['passcode']
        cursor.execute("SELECT * FROM users WHERE name = %s AND passcode = %s", (name, passcode))
        record = cursor.fetchone()
        if record and name == record[1]:
            session['loggedin'] = True
            session['name'] = record[1]        
            username = record[1]
            return redirect(url_for('management_bp.management', username = username))
        else:
            session.pop('loggedin', None)
            session.pop('name', None)
            msg = 'Invalid username or password'
    return render_template('auth/index.html', msg=msg)

def logout_user():
    session.pop('loggedin', None)
    session.pop('name', None)
    return redirect(url_for('authen.auth'))