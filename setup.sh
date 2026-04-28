#!/bin/bash
set -e

# Create instance directory if it doesn't exist
mkdir -p instance

# Import data only if database doesn't exist or is empty
python import_data.py

# Start the app
gunicorn wsgi:app
