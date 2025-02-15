### update.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title='1984')
>>> book.title = 'Nineteen Eighty-Four'
>>> book.save()
>>> print("Updated Book:", book)
Updated Book: Nineteen Eighty-Four, George Orwell, 1949