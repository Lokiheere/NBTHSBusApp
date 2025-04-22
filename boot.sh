#!/bin/bash

set -e

echo "Starting uWSGI..."
exec uwsgi --ini /config/app.ini