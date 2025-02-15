### delete.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title='Nineteen Eighty-Four')
>>> book.delete()
>>> print("Book deleted successfully.")
Book deleted successfully.
>>> books = Book.objects.all()
>>> print("Remaining Books:", books)
Remaining Books: <QuerySet []>
