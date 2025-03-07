from flask import Flask, render_template
from .data import admin_data_handler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('layout.html')

@app.route('/auth')
def auth():
    data = admin_data_handler.get_db()
    return render_template('auth/index.html', data=data)

@app.route('/home')
def home():
    return render_template('home/index.html')