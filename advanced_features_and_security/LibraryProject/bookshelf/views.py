from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms 

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data["query"]
        # Using ORM to avoid SQL injection
        books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect("book_list")
    return render(request, "bookshelf/book_form.html")


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/book_form.html", {"book": book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
