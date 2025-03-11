from django.urls import path
from .views import BookListView

urlpatterns = [
    path('book/', BookListView.as_view(), name='book-list-view'),
]