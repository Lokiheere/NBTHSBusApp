import os

import folium
from app.utils.db_connect import get_connection

SPOT_LOCATION = {
    "Spot A": [40.45278217829758, -74.46772714669649],
    "Spot B": [40.45279035227332, -74.46772714669649],
    "Spot C": [40.45347406930079, -74.46786208465576],
    "Spot E": [40.45279035227332, -74.46775167638062],
    "Spot D": [40.452805934846104, -74.46773150528614],
    "Spot F": [40.452805934846104 ,-74.46776],
}


def get_spot_location(selected_spot):
    return SPOT_LOCATION.get(selected_spot, None)


def bus_setup():
    """
    sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    with get_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT bus_name, spot_name FROM assigned_buses")
            assigned_data = cursor.fetchall()

    for item in assigned_data:
        item["location"] = get_spot_location(item["spot_name"])

    return assigned_data


def reset_map() -> None:
    """
    sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM assigned_buses")

            connection.commit()

    if os.path.exists("app/static/maps/"):
        for file in os.listdir("app/static/maps/"):
            file_path = os.path.join("app/static/maps/", file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            else:
                print("Failed to remove {} as it didn't exist".format(file_path))


def render_map():
    """
    sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    assigned_data = bus_setup()

    print(bus_setup())

    for bus in assigned_data:
        if bus["location"]:
            plan = folium.Map(
                location=bus["location"],
                zoom_start=19,
                zoom_control=False,
                dragging=False,
                scrollWheelZoom=False,
                doubleClickZoom=False,
                no_touch=True,
            )

            folium.Marker(
                location=bus["location"],
                popup=folium.Popup(f"Bus: {bus['bus_name']} - Spot: {bus['spot_name']}", max_width=250),
                icon=folium.CustomIcon(icon_image="app/static/img/bus_icon.png", icon_size=(20, 20)),
            ).add_to(plan)

            map_filename = f"app/static/maps/map_{bus['bus_name']}_{bus['spot_name']}.html"

            plan.save(map_filename)
    return assigned_data