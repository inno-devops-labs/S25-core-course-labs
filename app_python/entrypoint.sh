#!/bin/sh
# Check if /app/visits exists and fix its permissions
if [ -d /app/visits ]; then
    echo "Fixing permissions on /app/visits"
    chown -R appuser:appgroup /app/visits
fi
exec python app.py

