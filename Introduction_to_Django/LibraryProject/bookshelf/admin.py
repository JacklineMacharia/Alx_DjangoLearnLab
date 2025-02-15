from django.contrib import admin
from.models import Book # Customizing the Admin Interface

class BookAdmin(admin.ModelAdmin):
    # Display the book's field in list form
    list_display = ('title', 'author', 'publication_year')
    #Adding filters for the list view
    list_filter = ('author', 'publication_year')
    #Enables search capabilities for the title and author field
    search_fields = ('title', 'author')

admin.site.register(Book)

# Register your models here.
