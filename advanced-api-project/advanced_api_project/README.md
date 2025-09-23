### API Endpoints for Book

- **List Books** → `GET /api/books/` (public)
- **Create Book** → `POST /api/books/` (authenticated)
- **Retrieve Book** → `GET /api/books/<id>/` (public)
- **Update Book** → `PUT/PATCH /api/books/<id>/` (authenticated)
- **Delete Book** → `DELETE /api/books/<id>/` (authenticated)

### Permissions
- Unauthenticated users: Read-only access
- Authenticated users: Full CRUD access


### Filtering, Searching, and Ordering

The `BookListView` supports advanced query parameters:

- **Filtering**  
  Example: `/books/?title=The Hobbit`  
  Example: `/books/?publication_year=2020`

- **Searching**  
  Example: `/books/?search=tolkien` (searches in title and author name)

- **Ordering**  
  Example: `/books/?ordering=publication_year`  
  Example: `/books/?ordering=-title` (descending)