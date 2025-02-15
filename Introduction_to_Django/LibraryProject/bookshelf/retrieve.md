### retrieve.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title='1984')
>>> print("Book details:", book)
Book details: 1984, George Orwell, 1949