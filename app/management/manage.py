import os
from app.utils.db_connect import get_connection
from flask import session

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

connection = get_connection(host, user, password, database, port)

cursor = connection.cursor()

def process_selection(selected_option, available_options):
    if selected_option in available_options:
        available_options.remove(selected_option)
        msg = f"Selected option: {selected_option}"
    else:
        msg = "Invalid selection. Please choose a valid option."
    return available_options, msg

from datetime import datetime

available_options = ['Task 1', 'Task 2', 'Task 3', 'Task 4']
original_options = available_options.copy()

def reset_options():
    available_options = original_options.copy()

    #Tawsif here just checking to see if the code works
    print(f"Options reset at {datetime.now()}, new options: {available_options}")

# from flask_wtf import FlaskForm
# from wtforms import SelectField, SubmitField
# from wtforms.validators import InputRequired

# class BusForm(FlaskForm):
#     bus_id = SelectField('Bus ID', choices=[], validators=[InputRequired()])
#     bus_location = SelectField('Bus Location', choices=[
#         ('Location1', 'Location1'),
#         ('Location2', 'Location2'),
#         ('Location3', 'Location3')
#     ], validators=[InputRequired()])
#     submit = SubmitField('Submit')

#     def __init__(self, *args, **kwargs):
#         super(BusForm, self).__init__(*args, **kwargs)
#         cursor.execute("SELECT bus_id FROM buses")
#         bus_ids = cursor.fetchall()
#         self.bus_id.choices = [(bus[0], bus[0]) for bus in bus_ids] 