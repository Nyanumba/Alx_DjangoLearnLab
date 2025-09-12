# Permissions & Groups Setup

## Custom Permissions
The `Book` model defines four permissions:
- `can_view`: View book entries
- `can_create`: Create new book entries
- `can_edit`: Edit existing book entries
- `can_delete`: Delete book entries

## Groups
- **Viewers**: Only `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Usage
Permissions are enforced in `bookshelf/views.py` using the `@permission_required` decorator.  
Example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    ...
