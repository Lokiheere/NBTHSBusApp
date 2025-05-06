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


def reset_map():
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

    plan = folium.Map(
        location=[40.453329, -74.467905],
        zoom_start=19,
        zoom_control=False,
        dragging=False,
        scrollWheelZoom=False,
        doubleClickZoom=False,
        no_touch=True,
    )

    plan.save("app/templates/maps/map1.html")


def render_map():
    """
    sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    assigned_data = bus_setup()

    print(bus_setup())

    plan = folium.Map(
        location=[40.453329, -74.467905],
        zoom_start=19,
        zoom_control=False,
        dragging=False,
        scrollWheelZoom=False,
        doubleClickZoom=False,
        no_touch=True,
    )

    for bus in assigned_data:
        if bus["location"]:
            folium.Marker(
                location=bus["location"],
                popup=folium.Popup(f"Bus: {bus['bus_name']} - Spot: {bus['spot_name']}", max_width=250),
                icon=folium.Icon(color="blue", icon="bus")
            ).add_to(plan)

    plan.save("app/templates/maps/map1.html")

#     tiles="cartodb positron",
