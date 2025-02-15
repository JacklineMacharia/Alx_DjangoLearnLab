### update.md
>>> book = Book.objects.get(title='1984')
>>> book.title = 'Nineteen Eighty-Four'
>>> book.save()
>>> print("Updated Book:", book)
Updated Book: Nineteen Eighty-Four