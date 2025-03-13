from rest_framework import serializers
from .models import Author, Book
import datetime

"""
BookSerializer:
- Serializes all Book fields.
- Includes validation to ensure the publication year is not in the future.

"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication year
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

"""
AuthorSerializer:
- Serializes Author fields along with a nested list of books using BookSerializer.
"""
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
