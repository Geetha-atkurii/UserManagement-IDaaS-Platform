# API Specification

## Authentication

POST /auth/login

POST /auth/logout

POST /auth/refresh

POST /auth/forgot-password

POST/auth/change-password
---

## Users

POST /users

GET /users

GET /users/{id}

PUT /users/{id}

DELETE /users/{id}

---

## Roles

POST /roles

GET /roles

PUT /roles/{id}

DELETE /roles/{id}

---

## Permissions

POST /permissions

GET /permissions

---

## Organizations

POST /organizations

GET /organizations/{organization_id}