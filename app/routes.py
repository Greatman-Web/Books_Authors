from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from app.models import Author, Book
from sqlalchemy import or_

main_bp = Blueprint('main', __name__)
author_bp = Blueprint('author', __name__, url_prefix='/authors')
book_bp = Blueprint('book', __name__, url_prefix='/books')

# ==================== MAIN ROUTES ====================

@main_bp.route('/')
def index():
    """Home page with statistics."""
    try:
        author_count = Author.query.count()
        book_count = Book.query.count()
        featured_authors = Author.query.limit(3).all()
        return render_template('index.html', 
                             author_count=author_count,
                             book_count=book_count,
                             featured_authors=featured_authors)
    except Exception as e:
        flash(f'Error loading homepage: {str(e)}', 'danger')
        return render_template('index.html', 
                             author_count=0,
                             book_count=0,
                             featured_authors=[])

# ==================== AUTHOR ROUTES ====================

@author_bp.route('/')
def list_authors():
    """List all authors with pagination."""
    try:
        page = request.args.get('page', 1, type=int)
        search = request.args.get('search', '', type=str)
        
        query = Author.query
        if search:
            query = query.filter(or_(
                Author.name.ilike(f'%{search}%'),
                Author.nationality.ilike(f'%{search}%')
            ))
        
        authors = query.paginate(page=page, per_page=10)
        return render_template('authors/list.html', authors=authors, search=search)
    except Exception as e:
        flash(f'Error loading authors: {str(e)}', 'danger')
        return render_template('authors/list.html', authors=[])

@author_bp.route('/<int:author_id>')
def view_author(author_id):
    """View author details and their books."""
    author = Author.query.get_or_404(author_id)
    books = author.books
    return render_template('authors/detail.html', author=author, books=books)

# ==================== BOOK ROUTES ====================

@book_bp.route('/')
def list_books():
    """List all books with pagination and filtering."""
    try:
        page = request.args.get('page', 1, type=int)
        search = request.args.get('search', '', type=str)
        genre = request.args.get('genre', '', type=str)
        
        query = Book.query
        
        if search:
            query = query.filter(or_(
                Book.title.ilike(f'%{search}%'),
                Book.description.ilike(f'%{search}%')
            ))
        
        if genre:
            query = query.filter(Book.genre.ilike(f'%{genre}%'))
        
        books = query.paginate(page=page, per_page=10)
        genres = db.session.query(Book.genre).distinct().filter(Book.genre != None).all()
        genres = [g[0] for g in genres]
        
        return render_template('books/list.html', 
                             books=books, 
                             search=search, 
                             genre=genre,
                             genres=genres)
    except Exception as e:
        flash(f'Error loading books: {str(e)}', 'danger')
        return render_template('books/list.html', books=[])

@book_bp.route('/<int:book_id>')
def view_book(book_id):
    """View book details."""
    book = Book.query.get_or_404(book_id)
    return render_template('books/detail.html', book=book)
