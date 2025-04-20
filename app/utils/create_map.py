import folium

# Example data for buses (locations and numbers)
bus_data = [
    {"number": "Bus 1", "location": [40.45270809342312, -74.4676765629711]},
    {"number": "Bus 2", "location": [40.4530533013997, -74.46776038200282]},
    {"number": "Bus 3", "location": [40.45347406930079, -74.46786208465576]}
]

# Create a Folium map with all buses
start_coords = [40.453329, -74.467905]
map = folium.Map(
    location=start_coords, 
    zoom_start=19,
    zoom_control=False,
    dragging=False,
    scrollWheelZoom=False,
    doubleClickZoom=False,
    no_touch=True,
)

# Add bus markers to the map
for bus in bus_data:
    folium.Marker(
        location=bus["location"],
        popup=f"{bus['number']}",
        icon=folium.Icon(color="blue", icon="bus")
    ).add_to(map)

# Save the map as HTML
map.save("app/templates/maps/map1.html")

# m = folium.Map(
#     location=[40.453329, -74.467905], 
#     tiles="cartodb positron", 
#     zoom_start=19,
#     zoom_control=False,
#     dragging=False,
#     scrollWheelZoom=False,
#     doubleClickZoom=False,
#     no_touch=True,
#     )

# m.save('app/templates/maps/map1.html')