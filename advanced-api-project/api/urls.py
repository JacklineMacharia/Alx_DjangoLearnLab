from django.urls import path
from .views import BookListView, CreateView, DetailView, UpdateView, DeleteView

urlpatterns = [
     path('books/', BookListView.as_view(), name='book-list'),
     path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
     path('books/create/', CreateView.as_view(), name='book-create'),
     path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
     path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]
