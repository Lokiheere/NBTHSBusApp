from flask import Flask, render_template
import os
from dotenv import load_dotenv 
from flask_admin import Admin
from tests.dashboard import UserView

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

load_dotenv('.env')

app.secret_key = os.getenv('SECRET_KEY')

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

admin = Admin(app, name='Admin Dashboard', template_mode='bootstrap3', base_template='admin/base.html')

admin.add_view(UserView(name='Users', endpoint='user_view'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    
# import folium

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