from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book

class BookAPITestCase(TestCase):
    """Unit tests for Book model CRUD operations."""

    def setUp(self):
        """Set up test data before each test runs."""
        self.client = APIClient()
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book_data = {
            "title": "Harry Potter",
            "publication_year": 1997,
            "author": self.author.id
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        """Test creating a new book."""
        response = self.client.post('/api/books/create/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_get_all_books(self):
        """Test retrieving all books."""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_update_book(self):
        """Test updating a book's title."""
        updated_data = {"title": "Harry Potter and the Chamber of Secrets"}
        response = self.client.patch(f'/api/books/{self.book.id}/update/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Chamber of Secrets")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
