from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout, authenticate
# register
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path

# logout
from django.contrib.auth.views import LogoutView


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
 
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
def RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'relationship_app/register.html'
      
urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]

urlpatterns += [  # Append logout URL to existing urlpatterns
    path('logout/', LogoutView.as_view(), name='logout'),
]