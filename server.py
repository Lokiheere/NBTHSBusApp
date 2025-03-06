from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('layout.html')

@app.route('/auth')
def auth():
    return render_template('auth/index.html')