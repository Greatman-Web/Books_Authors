from app import db
from datetime import datetime

class Author(db.Model):
    """Author model."""
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True, index=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    nationality = db.Column(db.String(100))
    biography = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    books = db.relationship('Book', backref='author', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Author {self.name}>'
    
    def get_book_count(self):
        """Return number of books by this author."""
        return len(self.books)


class Book(db.Model):
    """Book model."""
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    publication_year = db.Column(db.Integer)
    isbn = db.Column(db.String(20), unique=True)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    genre = db.Column(db.String(100))
    pages = db.Column(db.Integer)
    language = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
    def get_author_name(self):
        """Return author name."""
        return self.author.name if self.author else 'Unknown'
