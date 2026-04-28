"""
Data import script for loading authors and books into the database.
This script can load data from CSV files or generate sample data.
"""

import os
import sys
import random
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from app.models import Author, Book

# Sample data
NATIONALITIES = [
    'American', 'British', 'French', 'German', 'Spanish', 'Italian', 
    'Russian', 'Japanese', 'Indian', 'Canadian', 'Australian', 'Irish',
    'Swedish', 'Norwegian', 'Danish', 'Dutch', 'Belgian', 'Swiss',
    'Portuguese', 'Greek', 'Polish', 'Czech', 'Turkish', 'Brazilian'
]

GENRES = [
    'Fiction', 'Mystery', 'Romance', 'Science Fiction', 'Fantasy', 'Thriller',
    'Historical Fiction', 'Biography', 'Self-Help', 'Poetry', 'Drama', 'Horror',
    'Adventure', 'Literary Fiction', 'Young Adult', 'Children', 'Graphic Novel'
]

LANGUAGES = ['English', 'French', 'German', 'Spanish', 'Italian', 'Russian', 'Japanese', 'Portuguese']

AUTHORS_DATA = [
    {'name': 'William Shakespeare', 'birth_year': 1564, 'death_year': 1616, 'nationality': 'British'},
    {'name': 'Jane Austen', 'birth_year': 1775, 'death_year': 1817, 'nationality': 'British'},
    {'name': 'Mark Twain', 'birth_year': 1835, 'death_year': 1910, 'nationality': 'American'},
    {'name': 'Leo Tolstoy', 'birth_year': 1828, 'death_year': 1910, 'nationality': 'Russian'},
    {'name': 'Charles Dickens', 'birth_year': 1812, 'death_year': 1870, 'nationality': 'British'},
    {'name': 'Fyodor Dostoevsky', 'birth_year': 1821, 'death_year': 1881, 'nationality': 'Russian'},
    {'name': 'Gustave Flaubert', 'birth_year': 1821, 'death_year': 1880, 'nationality': 'French'},
    {'name': 'George Eliot', 'birth_year': 1819, 'death_year': 1880, 'nationality': 'British'},
    {'name': 'Victor Hugo', 'birth_year': 1802, 'death_year': 1885, 'nationality': 'French'},
    {'name': 'Ernest Hemingway', 'birth_year': 1899, 'death_year': 1961, 'nationality': 'American'},
    {'name': 'F. Scott Fitzgerald', 'birth_year': 1896, 'death_year': 1940, 'nationality': 'American'},
    {'name': 'George Orwell', 'birth_year': 1903, 'death_year': 1950, 'nationality': 'British'},
    {'name': 'Virginia Woolf', 'birth_year': 1882, 'death_year': 1941, 'nationality': 'British'},
    {'name': 'James Joyce', 'birth_year': 1882, 'death_year': 1941, 'nationality': 'Irish'},
    {'name': 'Haruki Murakami', 'birth_year': 1949, 'death_year': None, 'nationality': 'Japanese'},
    {'name': 'Gabriel García Márquez', 'birth_year': 1927, 'death_year': 2014, 'nationality': 'Colombian'},
    {'name': 'Paulo Coelho', 'birth_year': 1947, 'death_year': None, 'nationality': 'Brazilian'},
    {'name': 'Margaret Atwood', 'birth_year': 1939, 'death_year': None, 'nationality': 'Canadian'},
    {'name': 'Toni Morrison', 'birth_year': 1931, 'death_year': 2019, 'nationality': 'American'},
    {'name': 'Salman Rushdie', 'birth_year': 1947, 'death_year': None, 'nationality': 'British'},
]

BOOK_TITLES_BY_AUTHOR = {
    'William Shakespeare': [
        'Hamlet', 'Romeo and Juliet', 'Macbeth', 'Othello', 'A Midsummer Night\'s Dream',
        'The Tempest', 'The Merchant of Venice', 'Much Ado About Nothing'
    ],
    'Jane Austen': [
        'Pride and Prejudice', 'Sense and Sensibility', 'Emma', 'Persuasion',
        'Northanger Abbey', 'Mansfield Park'
    ],
    'Mark Twain': [
        'The Adventures of Tom Sawyer', 'Adventures of Huckleberry Finn',
        'The Prince and the Pauper', 'A Connecticut Yankee in King Arthur\'s Court'
    ],
    'Leo Tolstoy': [
        'War and Peace', 'Anna Karenina', 'The Cossacks', 'Resurrection'
    ],
    'Charles Dickens': [
        'A Tale of Two Cities', 'Great Expectations', 'Oliver Twist',
        'A Christmas Carol', 'David Copperfield'
    ],
}

def generate_sample_authors():
    """Generate sample authors."""
    authors = []
    
    # Add predefined authors
    for author_data in AUTHORS_DATA:
        author = Author(
            name=author_data['name'],
            birth_year=author_data.get('birth_year'),
            death_year=author_data.get('death_year'),
            nationality=author_data.get('nationality'),
            biography=f"A renowned author from {author_data.get('nationality')}."
        )
        authors.append(author)
    
    # Generate additional authors to reach ~2000 books
    # With multiple books per author, we need ~100-200 authors
    base_names = ['John', 'Mary', 'James', 'Patricia', 'Robert', 'Jennifer',
                  'Michael', 'Linda', 'William', 'Barbara', 'David', 'Elizabeth']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia',
                  'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Taylor', 'Anderson']
    
    author_count = len(authors)
    while author_count < 150:
        first_name = random.choice(base_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        
        # Ensure unique names
        if not any(a.name == name for a in authors):
            author = Author(
                name=name,
                birth_year=random.randint(1800, 2000),
                nationality=random.choice(NATIONALITIES),
                biography=f"Author of various {random.choice(GENRES).lower()} works."
            )
            authors.append(author)
            author_count += 1
    
    return authors

def generate_sample_books(authors):
    """Generate sample books for authors."""
    books = []
    
    # Add predefined books for famous authors
    for author in authors:
        if author.name in BOOK_TITLES_BY_AUTHOR:
            titles = BOOK_TITLES_BY_AUTHOR[author.name]
            for idx, title in enumerate(titles):
                book = Book(
                    title=title,
                    author=author,
                    publication_year=random.randint(max(1500, author.birth_year if author.birth_year else 1500), 2023),
                    isbn=f"978{random.randint(1000000000, 9999999999)}",
                    description=f"A classic work by {author.name}. This book is a masterpiece of literature.",
                    rating=random.uniform(3.5, 5.0),
                    genre=random.choice(GENRES),
                    pages=random.randint(150, 800),
                    language=random.choice(LANGUAGES)
                )
                books.append(book)
    
    # Generate additional books to reach ~2000+ records
    while len(books) < 2500:
        author = random.choice(authors)
        book_number = len([b for b in books if b.author_id == author.id]) + 1
        
        book = Book(
            title=f"The {random.choice(['Mystery', 'Quest', 'Adventure', 'Tale', 'Story'])} of {author.name.split()[-1]} - Book {book_number}",
            author=author,
            publication_year=random.randint(max(1900, author.birth_year if author.birth_year else 1900), 2023),
            isbn=f"978{random.randint(1000000000, 9999999999)}",
            description=f"An engaging {random.choice(GENRES).lower()} novel by {author.name}. "
                       f"This captivating work explores themes of {random.choice(['love', 'adventure', 'mystery', 'discovery'])}.",
            rating=round(random.uniform(2.5, 5.0), 1),
            genre=random.choice(GENRES),
            pages=random.randint(100, 1000),
            language=random.choice(LANGUAGES)
        )
        books.append(book)
    
    return books

def import_data():
    """Import sample data into database."""
    # Use production config if DATABASE_URL is set (Render)
    env = 'production' if os.environ.get('DATABASE_URL') else 'development'
    app = create_app(env)
    
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        Book.query.delete()
        Author.query.delete()
        db.session.commit()
        
        # Generate and import data
        print("Generating authors...")
        authors = generate_sample_authors()
        db.session.add_all(authors)
        db.session.commit()
        print(f"✓ Created {len(authors)} authors")
        
        print("Generating books...")
        books = generate_sample_books(authors)
        db.session.add_all(books)
        db.session.commit()
        print(f"✓ Created {len(books)} books")
        
        # Print statistics
        print("\n" + "="*50)
        print("DATABASE IMPORT COMPLETE")
        print("="*50)
        print(f"Total Authors: {Author.query.count()}")
        print(f"Total Books: {Book.query.count()}")
        print(f"Average books per author: {Book.query.count() / Author.query.count():.1f}")
        print("="*50)

if __name__ == '__main__':
    import_data()
