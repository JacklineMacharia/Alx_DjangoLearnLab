from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView, ListFollowersView, ListFollowingView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('followers/<int:id>/', ListFollowersView.as_view(), name='list-followers'),
    path('following/<int:id>/', ListFollowingView.as_view(), name='list-following'),
]
