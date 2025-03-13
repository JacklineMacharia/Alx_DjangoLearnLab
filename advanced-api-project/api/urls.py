from django.urls import path
from .views import BookListView, CreateView, Detailview, UpdateView, DeleteView

urlpatterns = [
     path('books/', BookListView.as_view(), name='book-list'),
     path('books/<int:pk>/', Detailview.as_view(), name='book-detail'),
     path('books/create/', CreateView.as_view(), name='book-create'),
     path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),
     path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
]
