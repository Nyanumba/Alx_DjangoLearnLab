from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="J.R.R. Tolkien")

        # Create books
        self.book1 = Book.objects.create(
            title="The Hobbit", publication_year=1937, author=self.author
        )
        self.book2 = Book.objects.create(
            title="The Lord of the Rings", publication_year=1954, author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.pk})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.pk})

    # ---------- List & Retrieve ----------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Hobbit")

    # ---------- Create ----------
    def test_create_book_unauthenticated(self):
        data = {"title": "Silmarillion", "publication_year": 1977, "author": self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "Silmarillion", "publication_year": 1977, "author": self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ---------- Update ----------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "The Hobbit - Updated", "publication_year": 1937, "author": self.author.pk}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "The Hobbit - Updated")

    # ---------- Delete ----------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- Filtering, Searching, Ordering ----------
    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=The Hobbit")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_search_books_by_author(self):
        response = self.client.get(f"{self.list_url}?search=tolkien")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("The Hobbit" in book["title"] for book in response.data))

    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "The Hobbit")
