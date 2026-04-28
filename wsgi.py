"""
WSGI entry point for production deployment.
"""

import os
from run import app

# Ensure instance folder exists
os.makedirs('instance', exist_ok=True)

if __name__ == "__main__":
    app.run()
