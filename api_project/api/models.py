from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    
    def __str__(self):
        return self.title

