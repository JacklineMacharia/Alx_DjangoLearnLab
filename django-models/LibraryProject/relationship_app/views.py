from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

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
   
    
def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
        else:
            form = AuthenticationForm()
        return render(request, 'relationship_app/login.html', {'form':form})
    
def LogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout')
    return render(request, 'relationship_app/logout.html')