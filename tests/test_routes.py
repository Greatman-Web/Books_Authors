"""
Tests for routes.
"""

import pytest

class TestMainRoutes:
    """Test main application routes."""
    
    def test_index(self, client):
        """Test the homepage."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Books & Authors' in response.data
        assert b'Featured Authors' in response.data
    
    def test_index_with_data(self, client, sample_author, sample_book):
        """Test homepage with sample data."""
        response = client.get('/')
        assert response.status_code == 200
        # Check that statistics are displayed
        assert b'Total Books' in response.data
        assert b'Total Authors' in response.data

class TestAuthorRoutes:
    """Test author-related routes."""
    
    def test_list_authors(self, client, sample_author):
        """Test listing authors."""
        response = client.get('/authors/')
        assert response.status_code == 200
        assert b'Authors' in response.data
        assert b'Test Author' in response.data
    
    def test_author_pagination(self, client, app):
        """Test author pagination."""
        from app import db
        from app.models import Author
        
        # Create 15 authors to test pagination
        for i in range(15):
            author = Author(name=f'Author {i}', nationality='American')
            db.session.add(author)
        db.session.commit()
        
        # First page
        response = client.get('/authors/?page=1')
        assert response.status_code == 200
        assert b'Author 0' in response.data
        
        # Second page
        response = client.get('/authors/?page=2')
        assert response.status_code == 200
    
    def test_author_search(self, client, sample_author):
        """Test author search functionality."""
        response = client.get('/authors/?search=Test')
        assert response.status_code == 200
        assert b'Test Author' in response.data
    
    def test_view_author(self, client, sample_author):
        """Test viewing a specific author."""
        response = client.get(f'/authors/{sample_author.id}')
        assert response.status_code == 200
        assert b'Test Author' in response.data
    
    def test_view_author_not_found(self, client):
        """Test viewing a non-existent author."""
        response = client.get('/authors/9999')
        assert response.status_code == 404

class TestBookRoutes:
    """Test book-related routes."""
    
    def test_list_books(self, client, sample_book):
        """Test listing books."""
        response = client.get('/books/')
        assert response.status_code == 200
        assert b'Books' in response.data
        assert b'Test Book' in response.data
    
    def test_book_search(self, client, sample_book):
        """Test book search functionality."""
        response = client.get('/books/?search=Test')
        assert response.status_code == 200
        assert b'Test Book' in response.data
    
    def test_book_genre_filter(self, client, app, sample_book):
        """Test book genre filtering."""
        from app import db
        from app.models import Book
        
        book = Book(
            title='Fiction Book',
            author_id=sample_book.author_id,
            genre='Mystery'
        )
        db.session.add(book)
        db.session.commit()
        
        response = client.get('/books/?genre=Mystery')
        assert response.status_code == 200
    
    def test_view_book(self, client, sample_book):
        """Test viewing a specific book."""
        response = client.get(f'/books/{sample_book.id}')
        assert response.status_code == 200
        assert b'Test Book' in response.data
        assert b'Test Author' in response.data
    
    def test_view_book_not_found(self, client):
        """Test viewing a non-existent book."""
        response = client.get('/books/9999')
        assert response.status_code == 404

class TestErrorHandling:
    """Test error handling."""
    
    def test_404_error(self, client):
        """Test 404 error page."""
        response = client.get('/nonexistent')
        assert response.status_code == 404
        assert b'404' in response.data or b'not found' in response.data.lower()
