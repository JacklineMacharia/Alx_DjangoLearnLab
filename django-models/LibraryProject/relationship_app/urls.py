from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', SignUpView.as_view(), name='register'),
        path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]
