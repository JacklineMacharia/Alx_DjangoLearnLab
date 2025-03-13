from django.db import models

# Create your models here.
"""
Author Model:
- Represents an author with a name field.
- Has a one-to-many relationship with books.

"""
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

"""Book Model:
- Represents a book with title and publication year.
- Links to an Author using a ForeignKey.
"""
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title