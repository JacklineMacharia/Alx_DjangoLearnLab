from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from api.models import Author, Book
from api.views import BookListView, DetailView, CreateView, UpdateView, DeleteView


class BookAPITestCase(TestCase):
    """
    Unit tests for Book model CRUD operations using APIRequestFactory.
    """

    def setUp(self):
        """
        Initialize test data and API request factory.
        """
        self.factory = APIRequestFactory()
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )
    
    def test_create_book(self):
        """
        Test creating a book using APIRequestFactory.
        """
        data = {
            "title": "Fantastic Beasts",
            "publication_year": 2016,
            "author": self.author.id
        }
        request = self.factory.post('/api/books/create/', data, format='json')
        response = CreateView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_all_books(self):
        """
        Test retrieving all books.
        """
        request = self.factory.get('/api/books/')
        response = BookListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_single_book(self):
        """
        Test retrieving a book by ID.
        """
        request = self.factory.get(f'/api/books/{self.book.id}/')
        response = DetailView.as_view()(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")


    def test_update_book(self):
        """
        Test updating a book title.
        """
        updated_data = {"title": "Harry Potter and the Chamber of Secrets"}
        request = self.factory.patch(f'/api/books/{self.book.id}/update/', updated_data, format='json')
        response = UpdateView.as_view()(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_book(self):
        """
        Test deleting a book.
        """
        request = self.factory.delete(f'/api/books/{self.book.id}/delete/')
        response = DeleteView.as_view()(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
