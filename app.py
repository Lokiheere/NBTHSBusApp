import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

from app import create_app
app = create_app()

from flask_socketio import SocketIO
socketio = SocketIO(app)
@socketio.on('connect')
def handle_connect():
    print("Client connected!")

from app.management.manage import reset_options

if __name__ == '__main__':
    scheduler.add_job(reset_options, 'cron', hour=24)

    scheduler.start()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

    