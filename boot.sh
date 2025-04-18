#!/bin/bash

set -e

echo "Starting uWSGI..."
exec uwsgi --ini app.ini