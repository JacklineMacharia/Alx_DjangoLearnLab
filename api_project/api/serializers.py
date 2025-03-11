from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.modelSerializer):
    class Meta:
        model = Book
        field = '__all__'