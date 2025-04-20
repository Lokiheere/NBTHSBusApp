from flask import Flask, render_template, request
import os

from flask_limiter import Limiter
limiter = Limiter(key_func=lambda: request.remote_addr)

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["DEBUG"] = True

    app.secret_key = os.getenv('SECRET_KEY')
    
    limiter.init_app(app)

    @app.route('/')
    def main():
        return render_template('main/index.html')

    from app.errors import error_handlers
    app.register_blueprint(error_handlers.error)

    from app.management import routes as management_routes
    app.register_blueprint(management_routes.management_bp)

    from app.auth import routes as auth_routes
    app.register_blueprint(auth_routes.authen)

    from app.home import routes as home_routes
    app.register_blueprint(home_routes.home_bp)
    
    import folium

    # Example data for buses (locations and numbers)
    bus_data = [
        {"number": "Bus 1", "location": [40.45270809342312, -74.4676765629711]},
        {"number": "Bus 2", "location": [40.45273125404057, -74.46776]},
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
    
    return app