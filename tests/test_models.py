"""
Tests for models.
"""

from app.models import Author, Book

class TestAuthorModel:
    """Test the Author model."""
    
    def test_author_creation(self, sample_author):
        """Test creating an author."""
        assert sample_author.id is not None
        assert sample_author.name == 'Test Author'
        assert sample_author.birth_year == 1980
        assert sample_author.nationality == 'American'
    
    def test_author_repr(self, sample_author):
        """Test Author string representation."""
        assert repr(sample_author) == '<Author Test Author>'
    
    def test_author_book_relationship(self, sample_author, sample_book):
        """Test the relationship between authors and books."""
        assert len(sample_author.books) == 1
        assert sample_author.books[0] == sample_book
        assert sample_book.author == sample_author
    
    def test_get_book_count(self, sample_author, sample_book, app):
        """Test getting book count for an author."""
        from app import db
        # Refresh the author to ensure the relationship is loaded
        db.session.refresh(sample_author)
        assert sample_author.get_book_count() == 1
        
        # Add another book
        book2 = Book(
            title='Test Book 2',
            author_id=sample_author.id,
            publication_year=2021,
            description='Another test book.'
        )
        db.session.add(book2)
        db.session.commit()
        
        # Refresh again to load the new book
        db.session.refresh(sample_author)
        assert sample_author.get_book_count() == 2

class TestBookModel:
    """Test the Book model."""
    
    def test_book_creation(self, sample_book):
        """Test creating a book."""
        assert sample_book.id is not None
        assert sample_book.title == 'Test Book'
        assert sample_book.publication_year == 2020
        assert sample_book.isbn == '978-0-123456-78-9'
    
    def test_book_repr(self, sample_book):
        """Test Book string representation."""
        assert repr(sample_book) == '<Book Test Book>'
    
    def test_get_author_name(self, sample_book):
        """Test getting author name from book."""
        assert sample_book.get_author_name() == 'Test Author'
    
    def test_book_cascade_delete(self, sample_author, sample_book, app):
        """Test that deleting an author deletes their books."""
        from app import db
        book_id = sample_book.id
        
        db.session.delete(sample_author)
        db.session.commit()
        
        assert Book.query.get(book_id) is None
