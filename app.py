#############################################################################
#                                                                           #
#                                                                           #
#    ████████╗███████╗ ██████╗██╗  ██╗ ██████╗██╗     ██╗   ██╗██████╗      #
#    ╚══██╔══╝██╔════╝██╔════╝██║  ██║██╔════╝██║     ██║   ██║██╔══██╗     #   
#       ██║   █████╗  ██║     ███████║██║     ██║     ██║   ██║██████╔╝     #
#       ██║   ██╔══╝  ██║     ██╔══██║██║     ██║     ██║   ██║██╔══██╗     #
#       ██║   ███████╗╚██████╗██║  ██║╚██████╗███████╗╚██████╔╝██████╔╝     #
#       ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝╚══════╝ ╚═════╝ ╚═════╝      #
#                                                                           #
#                                                                           #                                  
#                                                                           #
#    Bus App - Made by TechClub                                           #
#    GitHub: https://github.com/Lokiheere/NBTHSBusApp                       #
#                                                                           #
#############################################################################

import os

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), 'config', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

from app import create_app, socketio  
app = create_app()

@socketio.on('connect')
def handle_connect():
    print("Client connected!")

from app.management.manage import reset_options
from app.utils.create_map import reset_map, bus_setup, get_spot_location, render_map

from app.utils.db_initializer import initialize_database
initialize_database()

if __name__ == '__main__':
    scheduler.add_job(reset_options, 'interval', seconds=30)
    scheduler.add_job(reset_map, 'interval', seconds=80)
    # scheduler.add_job(bus_setup, 'interval', seconds=35)
    # scheduler.add_job(render_map, 'interval', seconds=40)

    scheduler.start()

    socketio.run(app, host="0.0.0.0",  port=8080)

#'cron', hour=0