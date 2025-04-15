#!/bin/sh
. venv/bin/activate

while true; do
    flask deploy
    if [ "$?" -eq 0 ]; then
        break
    fi
    echo failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - NBTHSbusapp:app