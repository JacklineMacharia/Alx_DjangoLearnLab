from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


class BookList(generic.ListAPIView): # type: ignore
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
