"""
Run the Flask application.
Usage: python run.py
"""

import os
from dotenv import load_dotenv
from app import create_app, db

load_dotenv()

app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
    
    # Run the application
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=os.environ.get('DEBUG', True), port=port, host='0.0.0.0')
