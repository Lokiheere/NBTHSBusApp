import os

from datetime import datetime
from app.utils.db_connect import get_connection

host= os.getenv('APP_HOST')
user= os.getenv('APP_USER')
password= os.getenv('APP_PASSWORD')
database= os.getenv('APP_DATABASE')
port= os.getenv('APP_PORT')

def process_selection(selected_bus, selected_spot):
    connection = get_connection(host, user, password, database, port)
    cursor = connection.cursor()

    cursor.execute("SELECT bus_name FROM buses WHERE bus_name = %s", (selected_bus,))
    bus_result = cursor.fetchone()

    cursor.execute("SELECT spot_name FROM parking_spots WHERE spot_name = %s", (selected_spot,))
    spot_result = cursor.fetchone()

    if bus_result and spot_result:
        cursor.execute("DELETE FROM buses WHERE bus_name = %s", (selected_bus,))
        cursor.execute("DELETE FROM parking_spots WHERE spot_name = %s", (selected_spot,))
        msg = f"Bus '{selected_bus}' and parking spot '{selected_spot}' were successfully removed."
    else:
        msg = "Invalid selection. Please choose valid options."

    connection.commit()  
    cursor.close()
    connection.close()

    return msg

def get_available_data():
    connection = get_connection(host, user, password, database, port)
    cursor = connection.cursor()

    cursor.execute("SELECT bus_name FROM buses")
    available_options = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT spot_name FROM parking_spots")
    parking_spots = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return available_options, parking_spots

def reset_options():
    connection = get_connection(host, user, password, database, port)
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM buses")
    default_bus_options = ['Bus 1', 'Bus 2', 'Bus 3', 'Bus 4']
    for bus in default_bus_options:
        cursor.execute("INSERT INTO buses (bus_name) VALUES (%s)", (bus,))
        
    cursor.execute("DELETE FROM parking_spots")
    default_parking_spots = ['Spot A', 'Spot B', 'Spot C', 'Spot D']
    for spot in default_parking_spots:
        cursor.execute("INSERT INTO parking_spots (spot_name) VALUES (%s)", (spot,))
        
    connection.commit()
    cursor.close()
    connection.close()

    #Tawsif here just checking to see if the code works
    print(f"Options reset at {datetime.now()}. Default buses and parking spots restored.")