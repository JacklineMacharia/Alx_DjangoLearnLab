from django.urls import path
from django.shortcuts import render
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views
from .views import PostDetailView, add_comment, CommentUpdateView, CommentDeleteView

app_name = "blog"
def base(request):
    return render(request, 'blog/base.html')

urlpatterns = [
    path('',  base, name='base'),  # This ensures the home page works
     path("register/", register_view, name="register"),
     path("login/", login_view, name="login"),
     path("logout/", logout_view, name="logout"),
     path("profile/", profile_view, name="profile"),
     
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/comment/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
