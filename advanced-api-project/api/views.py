from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books or create a new book
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Retrieve all books.
    POST: Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to view, but restrict creation to authenticated users
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve, update, or delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a book by ID.
    PUT/PATCH: Update a book (authenticated users only).
    DELETE: Delete a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
