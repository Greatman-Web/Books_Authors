import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Author, Book

@pytest.fixture(scope='function')
def app():
    """Create and configure a test instance of the app."""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    """Test client for the app."""
    return app.test_client()

@pytest.fixture(scope='function')
def runner(app):
    """Test CLI runner for the app."""
    return app.test_cli_runner()

@pytest.fixture(scope='function')
def sample_author(app):
    """Create a sample author."""
    author = Author(
        name='Test Author',
        birth_year=1980,
        nationality='American',
        biography='A test author.'
    )
    db.session.add(author)
    db.session.commit()
    return author

@pytest.fixture(scope='function')
def sample_book(app, sample_author):
    """Create a sample book."""
    book = Book(
        title='Test Book',
        author_id=sample_author.id,
        publication_year=2020,
        isbn='978-0-123456-78-9',
        description='A test book.',
        rating=4.5,
        genre='Fiction',
        pages=300,
        language='English'
    )
    db.session.add(book)
    db.session.commit()
    return book
