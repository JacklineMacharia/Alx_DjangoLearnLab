### create.md
>>> from bookshelf.models import Book
>>> book = Book(title='1984', authork='George Orwell', publication_year=1='George Orwell', publ949)
>>> book.save()
>>> print("Book created:", book)    
Book created: 1984

### retrieve.md
>>> book = Book.objects.get(title='1984')
>>> print("Retrieved Book:", book)
Retrieved Book: 1984

### update.md
>>> book = Book.objects.get(title='1984')
>>> book.title = 'Nineteen Eighty-Four'
>>> book.save()
>>> print("Updated Book:", book)
Updated Book: Nineteen Eighty-Four

### delete.md
>>> book = Book.objects.get(title='Nineteen Eighty-Four')
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> print("Book deleted successfully.")
Book deleted successfully.
>>> books = Book.objects.all()
>>> print("Remaining Books:", books)
Remaining Books: <QuerySet []>
