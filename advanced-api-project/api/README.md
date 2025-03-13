# Django REST API - Advanced API Project

## Description
This project is a Django REST API for managing books and authors using Django REST Framework (DRF).

## API Endpoints
- `GET /books/` - Retrieve all books (public)
- `GET /books/<id>/` - Retrieve a single book (public)
- `POST /books/create/` - Add a book (authenticated users only)
- `PUT /books/<id>/update/` - Update a book (authenticated users only)
- `DELETE /books/<id>/delete/` - Delete a book (authenticated users only)


## API Features: Filtering, Searching, and Ordering

### Filtering:
Use query parameters to filter books by:
- Title: `/api/books/?title=Harry Potter`
- Author name: `/api/books/?author__name=J.K. Rowling`
- Publication Year: `/api/books/?publication_year=2020`

### Searching:
Perform text search on title and author name:
- `/api/books/?search=Harry`

### Ordering:
Sort books by:
- Title (ascending): `/api/books/?ordering=title`
- Publication Year (descending): `/api/books/?ordering=-publication_year`


## Running Unit Tests

To ensure the API functions correctly, we have implemented automated tests using Django's `unittest` module.

### Running Tests
Activate your virtual environment:
```bash
venv\Scripts\activate     # On Windows
