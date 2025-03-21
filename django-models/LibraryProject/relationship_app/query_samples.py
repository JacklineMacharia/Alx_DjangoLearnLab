from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author Name"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name, ":", books_by_author)

# List all books in a library
library_name = "Library Name"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in", library_name, ":", books_in_library)

# # Retrieve the librarian for a library without using Librarian.objects.get(library=)
librarian_name = Librarian.objects.filter(library__name=library_name).values_list('name', flat=True).first()
print("Librarian for", library_name, ":", librarian_name)