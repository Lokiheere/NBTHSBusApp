from flask import render_template, request, session, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(".env")

def connection(host, user, password, database, port): 
    return mysql.connector.connect(
        host= host,
        user= user,
        password= password,
        database= database,
        port= port, 
    )

host= os.getenv('HOST')
user= os.getenv('USER')
password= os.getenv('PASSWORD')
database= os.getenv('DATABASE')
port= os.getenv('PORT')

connection = connection(host, user, password, database, port)

cursor = connection.cursor()

def login_user():
    msg = ''
    if request.method == 'POST':
        name = request.form['name']
        passcode = request.form['passcode']
        cursor.execute("SELECT * FROM passcode WHERE name = %s AND passcode = %s", (name, passcode))
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['name'] = record[1]
            return redirect(url_for('home'))
        else:
            msg = 'Invalid username or password'
    return render_template('auth/index.html', msg=msg)

def logout_user():
    session.pop('loggedin', None)
    session.pop('name', None)
    return redirect(url_for('auth'))