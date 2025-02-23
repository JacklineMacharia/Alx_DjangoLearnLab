from django.urls import path
from .views import register, login_view, logout_view, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', login_view.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view.as_view(template_name='logout.html'), name='logout'),]
