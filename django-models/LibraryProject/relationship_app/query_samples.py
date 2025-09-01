from relationship_app.models import Author, Librarian, Library, Book

# get all books by specifi author
def get_books_by_author(author_name):
    author = Author.objects.get(name = author_name)
    return author.books.all() 

# get all books in a library

def get_books_in_libary(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# get the librarian for a specific library

def get_librarian_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian