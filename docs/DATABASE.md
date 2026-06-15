# Database Design

## Organizations

Stores SaaS customers.

Columns:

- id
- name
- api_key
- plan
- status

---

## Users

Stores users belonging to organizations.

Columns:

- id
- organization_id
- email
- phone
- password_hash

---

## Roles

Organization-specific roles.

Examples:

- Admin
- Manager
- Doctor
- Teacher

---

## Permissions

Examples:

- create_user
- delete_user
- view_reports

---

## Future Tables

- user_roles
- role_permissions
- refresh_tokens
- audit_logs