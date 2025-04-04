from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from django.contrib.auth import get_user_model

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs(post=self.kwargs["post_id"]).order_by("-created_at"))
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class UserFeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
