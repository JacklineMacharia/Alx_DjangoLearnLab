from django.urls import path
from django.shortcuts import render
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views

app_name = "blog"
def base(request):
    return render(request, 'blog/base.html')

urlpatterns = [
    path('',  base, name='base'),  # This ensures the home page works
     path("register/", register_view, name="register"),
     path("login/", login_view, name="login"),
     path("logout/", logout_view, name="logout"),
     path("profile/", profile_view, name="profile"),
]
