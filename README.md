# 📚 Books & Authors Database Application

A Flask web application for browsing and searching 2,500+ books and 150+ authors from around the world. Built with Flask, SQLAlchemy, and Bootstrap 5.

## ✨ Features

- 📖 Browse 2,500+ books and 150+ authors
- 🔍 Full-text search by title, author name, or keyword
- 🏷️ Filter books by genre
- 📄 View detailed information about books and authors
- 💾 SQLite database with SQLAlchemy ORM
- 🎨 Responsive Bootstrap 5 interface
- ⚠️ Comprehensive error handling (404, 500, 400, 403)
- 🧪 Full test suite (22 unit & integration tests)
- 📱 Mobile-friendly design

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip package manager

### Installation & Setup

1. **Activate virtual environment**
   ```bash
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate # macOS/Linux
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Load database** (first time only)
   ```bash
   python import_data.py
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

Press `CTRL+C` to stop the server.

## 📖 Using the Application

### Navigation
- **Home**: View statistics and featured authors
- **Authors**: Browse 150+ authors, search by name or nationality
- **Books**: Browse 2,500+ books, filter by genre, search by title

### Key Features
- **Pagination**: All lists show 10 items per page
- **Search**: Global search on authors and books
- **Genre Filter**: Filter books by category (Fiction, Mystery, Science Fiction, etc.)
- **Links**: Click author names to view all their books
- **Details**: View complete information including ISBN, rating, and description

## 🧪 Testing

Run the test suite:
```bash
pytest tests/ -v              # Run all tests with verbose output
pytest tests/ --cov=app       # Run with coverage report
pytest tests/test_models.py   # Run specific test file
```

**Coverage**: 22 tests covering models, routes, and integration

## 📁 Project Structure

```
advanced/
├── app/                    # Flask application
│   ├── __init__.py        # Flask factory & config
│   ├── models.py          # Author & Book models
│   ├── routes.py          # Web routes
│   ├── errors.py          # Error handlers
│   ├── templates/         # HTML templates (8 files)
│   └── static/
│       └── css/style.css  # Bootstrap styling
├── tests/                 # Test suite (22 tests)
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_routes.py
│   └── test_integration.py
├── instance/
│   └── app.db            # SQLite database
├── config.py             # Configuration settings
├── run.py                # Entry point
├── import_data.py        # Data loader
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | Flask 3.0.0 |
| Database | SQLAlchemy + SQLite |
| Frontend | Bootstrap 5 + Jinja2 |
| Testing | pytest |
| Server | Gunicorn (production) |

## 📊 Database

**Authors Table**: 150 records with name, nationality, birth/death year, biography
**Books Table**: 2,500 records with title, genre, rating, ISBN, description

Each book is linked to one author. One author can have multiple books.

## 🔧 Application Components

### Configuration (config.py)
- Development, Testing, and Production configurations
- Database URL management
- Environment-based settings

### Models (app/models.py)
- `Author` model with book relationship
- `Book` model with author reference
- Helper methods for data retrieval

### Routes (app/routes.py)
- Main blueprint: Homepage
- Author blueprint: Author listing and details
- Book blueprint: Book listing and details
- Search and filtering functionality

### Error Handling (app/errors.py)
- 404 Not Found
- 500 Internal Server Error
- 400 Bad Request
- 403 Forbidden

### Templates
- Responsive Bootstrap 5 design
- Consistent navigation and footer
- Pagination for lists
- Search and filter forms

## 🌐 Deployment to Render

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push origin main
   ```

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`
   - Instance Type: Free

4. **Deploy** and visit your URL

## 🐛 Troubleshooting

**ModuleNotFoundError**: Activate virtual environment
```bash
pip install -r requirements.txt
```

**Port Already in Use**: Change port in `run.py` or use:
```bash
python run.py --port 5001
```

**Reset Database**: Delete `instance/app.db` and run:
```bash
python import_data.py
```

## 📦 Dependencies

Flask 3.0.0, Flask-SQLAlchemy 3.1.1, Flask-Migrate 4.0.5, python-dotenv 1.0.0, pytest 7.4.3

See `requirements.txt` for complete list.

## 📝 License

MIT License - Open source project

## ✅ Completion Status

- [x] Database-driven Flask app with 2+ linked tables
- [x] 2,500+ records loaded
- [x] Responsive Bootstrap 5 templates
- [x] Comprehensive error handling
- [x] Well-organized codebase
- [x] Full test suite (22 tests)
- [x] Git version control ready
- [x] Deployment configuration (Render)
- [x] Complete documentation

---

**Version**: 1.0.0 | **Last Updated**: April 2026
