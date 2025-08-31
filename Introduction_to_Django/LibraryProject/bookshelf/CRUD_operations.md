# CREATE
from bookshelf.models import Book

# Create a new book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output: <Book: 1984 by George Orwell (1949)>

# Retrieve
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected Output: ('1984', 'George Orwell', 1949)

# UPDATE
from bookshelf.models import Book

# Update title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Expected Output: 'Nineteen Eighty-Four'

# DELETE
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Expected Output: <QuerySet []>
