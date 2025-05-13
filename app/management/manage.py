from datetime import datetime

import mysql
from flask import request
from flask_wtf.csrf import validate_csrf

from app.utils.db_connect import get_connection
from app.utils.create_map import render_map


def process_selection(selected_bus, selected_spot) -> str:
    with get_connection() as connection:
        try:
            validate_csrf(request.form['csrf_token'])
            connection.ping(reconnect=True)
        except mysql.connector.Error as e:
            print(f"MySQL Error: {str(e)}")
            connection.rollback()

        with connection.cursor() as cursor:
            try:
                connection.autocommit = False

                cursor.execute("SELECT bus_name FROM buses WHERE bus_name = %s", (selected_bus,))
                bus_result = cursor.fetchone()

                cursor.execute("SELECT spot_name FROM parking_spots WHERE spot_name = %s", (selected_spot,))
                spot_result = cursor.fetchone()

                if bus_result and spot_result:
                    cursor.execute("INSERT INTO assigned_buses (bus_name, spot_name) VALUES (%s, %s)",
                                   (selected_bus, selected_spot))
                    cursor.execute("DELETE FROM buses WHERE bus_name = %s", (selected_bus,))
                    cursor.execute("DELETE FROM parking_spots WHERE spot_name = %s", (selected_spot,))
                    msg = f"Bus '{selected_bus}' and parking spot '{selected_spot}' were successfully added to the map."

                    connection.commit()

                    render_map()

                    return msg
                else:
                    msg = "Invalid selection. Please choose valid options."

                    return msg
            except:
                connection.rollback()

            msg = f"Error: {str(Exception)}"

    return msg


def get_available_data():
    """
    Fetches available bus names and parking spot names from the database.

    This function connects to the MySQL database, retrieves all bus names from the 'buses' table
    and all parking spot names from the 'parking_spots' table, then returns them as lists.

    Keyword arguments:
    None -- N/A

    Returns:
        - available_options (list): List of bus names.
        - parking_spots (list): List of parking spot names.
    """

    with get_connection() as connection:
        try:
            connection.ping(reconnect=True)
        except mysql.connector.Error as e:
            print(f"MySQL Error: {str(e)}")
            connection.rollback()

        with connection.cursor() as cursor:
            cursor.execute("SELECT bus_name FROM buses")
            available_options = [row[0] for row in cursor.fetchall()]

            cursor.execute("SELECT spot_name FROM parking_spots")
            parking_spots = [row[0] for row in cursor.fetchall()]
            cursor.close()
            connection.close()

    return available_options, parking_spots


def undo_selection(selected_bus_undo, selected_spot_undo):
    with get_connection() as connection:
        try:
            connection.ping(reconnect=True)
        except mysql.connector.Error as e:
            print(f"MySQL Error: {str(e)}")
            connection.rollback()

        with connection.cursor() as cursor:
            connection.autocommit = False
            cursor.execute("DELETE FROM assigned_buses WHERE bus_name = %s AND spot_name = %s ", (selected_bus_undo, selected_spot_undo))
            cursor.execute("INSERT INTO buses (bus_name) VALUES (%s)", (selected_bus_undo,))
            cursor.execute("INSERT INTO parking_spots  (spot_name) VALUES (%s)", (selected_spot_undo,))

            connection.commit()


def reset_options() -> None:
    """
    Resets the bus and parking spot MySQL database data to default at midnight.
    This function is called by the scheduler in app.py.
    This is to ensure that the options are always available for the next day.

    Keyword arguments:
    none -- N/A
    None: N/A
    """

    with get_connection() as connection:
        try:
            connection.ping(reconnect=True)
        except mysql.connector.Error as e:
            print(f"MySQL Error: {str(e)}")
            connection.rollback()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM buses")
            default_bus_options = ['Bus 1', 'Bus 2', 'Bus 3', 'Bus 4', 'Bus 5', 'Bus 6', 'Bus 7', 'Bus 8', 'Bus 9',
                                   'Bus 10', 'Bus 11', 'Bus 12', 'Bus 13', 'Bus 14', 'Bus 15', 'Bus 16', 'Bus 17',
                                   'Bus 18', 'Bus 19', 'Bus 20', 'Bus 21', 'Bus 22', 'Bus 23', 'Bus 24', 'Bus 25',
                                   'Bus 26', 'Bus 27', 'Bus 28', 'Bus 29', 'Bus 30', 'Bus 31', 'Bus 32']
            for bus in default_bus_options:
                cursor.execute("INSERT INTO buses (bus_name) VALUES (%s)", (bus,))

            cursor.execute("DELETE FROM parking_spots")
            default_parking_spots = ['Spot A', 'Spot B', 'Spot C', 'Spot D', 'Spot E', 'Spot F', 'Spot G', 'Spot H',
                                     'Spot I', 'Spot J', 'Spot K', 'Spot L', 'Spot M', 'Spot N', 'Spot O', 'Spot P',
                                     'Spot Q', 'Spot R', 'Spot S', 'Spot T', 'Spot U', 'Spot V', 'Spot W', 'Spot X',
                                     'Spot Y', 'Spot Z']
            for spot in default_parking_spots:
                cursor.execute("INSERT INTO parking_spots (spot_name) VALUES (%s)", (spot,))

            connection.commit()

    # Tawsif here just checking to see if the code works
    print(f"Options reset at {datetime.now()}. Default buses and parking spots restored.")
