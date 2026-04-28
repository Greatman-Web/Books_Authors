"""
Integration tests for the application.
"""

from app.models import Author, Book

def test_full_application_workflow(client, app):
    """Test a complete workflow through the application."""
    from app import db
    
    # 1. Homepage should load
    response = client.get('/')
    assert response.status_code == 200
    
    # 2. Create an author
    author = Author(
        name='Test Integration Author',
        birth_year=1990,
        nationality='British'
    )
    db.session.add(author)
    db.session.commit()
    
    # 3. Create books for the author
    for i in range(3):
        book = Book(
            title=f'Integration Test Book {i}',
            author_id=author.id,
            publication_year=2020 + i,
            genre='Fiction'
        )
        db.session.add(book)
    db.session.commit()
    
    # 4. View authors list
    response = client.get('/authors/')
    assert response.status_code == 200
    assert b'Test Integration Author' in response.data
    
    # 5. View specific author
    response = client.get(f'/authors/{author.id}')
    assert response.status_code == 200
    assert b'Test Integration Author' in response.data
    assert response.data.count(b'Integration Test Book') >= 3
    
    # 6. View books list
    response = client.get('/books/')
    assert response.status_code == 200
    assert b'Integration Test Book' in response.data
    
    # 7. View specific book
    book = Book.query.first()
    response = client.get(f'/books/{book.id}')
    assert response.status_code == 200
    assert b'Integration Test Book' in response.data
    assert b'Test Integration Author' in response.data
    
    # 8. Search functionality
    response = client.get('/authors/?search=Integration')
    assert response.status_code == 200
    assert b'Test Integration Author' in response.data
