### delete.md
>>> book = Book.objects.get(title='Nineteen Eighty-Four')
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> print("Book deleted successfully.")
Book deleted successfully.
>>> books = Book.objects.all()
>>> print("Remaining Books:", books)
Remaining Books: <QuerySet []>
