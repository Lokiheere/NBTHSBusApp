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
    
# import folium

# bus_data = [
#     {"number": "Bus 1", "location": [40.45270809342312, -74.4676765629711]},
#     {"number": "Bus 2", "location": [40.45273125404057, -74.46776]},
#     {"number": "Bus 3", "location": [40.45347406930079, -74.46786208465576]}
# ]

# start_coords = [40.453329, -74.467905]
# map = folium.Map(
#     location=start_coords, 
#     zoom_start=19,
#     zoom_control=False,
#     dragging=False,
#     scrollWheelZoom=False,
#     doubleClickZoom=False,
#     no_touch=True,
# )

# for bus in bus_data:
#     folium.Marker(
#         location=bus["location"],
#         popup=f"{bus['number']}",
#         icon=folium.Icon(color="blue", icon="bus")
#     ).add_to(map)

# map.save("app/templates/maps/map1.html")