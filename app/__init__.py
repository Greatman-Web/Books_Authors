from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes import main_bp, author_bp, book_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(book_bp)
    
    # Error handlers
    from app.errors import register_error_handlers
    register_error_handlers(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
