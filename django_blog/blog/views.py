from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms

# Create your views here.
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        
    def register_view(request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("blog:profile")
        else:
            form = RegisterForm()
        return render(request, "blog/register.html", {"form": form})
    
    def login_view(request):
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect("blog:profile")
        else:
            form = AuthenticationForm()
        return render(request, "blog/login.html", {"form": form})
    
    def logout_view(request):
        logout(request)
        return redirect("blog: login")
    
    def profile_view(request):
        return render(request, "blog/profile.html", {"user": request.user})
        
    @login_required
    def edit_profile_view(request):
        if request.method == "POST":
            form = UserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect("blog:profile")
        else:
            form = UserChangeForm(instance=request.user)
        return render(request, "blog/edit_profile.html", {"form": form})
            