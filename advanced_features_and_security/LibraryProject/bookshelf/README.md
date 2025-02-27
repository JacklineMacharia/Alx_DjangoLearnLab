# Django Permissions and Groups

## Custom Permissions:
- can_view → Allows users to view books.
- can_create → Allows users to create books.
- can_edit → Allows users to edit books.
- can_delete → Allows users to delete books.

## User Groups:
- **Viewers** → Can only view books.
- **Editors** → Can view, create, and edit books.
- **Admins** → Can view, create, edit, and delete books.

## How to Test:
1. Create users in Django admin.
2. Assign them to a group (`Viewers`, `Editors`, or `Admins`).
3. Login as different users and test access.
