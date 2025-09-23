### API Endpoints for Book

- **List Books** → `GET /api/books/` (public)
- **Create Book** → `POST /api/books/` (authenticated)
- **Retrieve Book** → `GET /api/books/<id>/` (public)
- **Update Book** → `PUT/PATCH /api/books/<id>/` (authenticated)
- **Delete Book** → `DELETE /api/books/<id>/` (authenticated)

### Permissions
- Unauthenticated users: Read-only access
- Authenticated users: Full CRUD access
