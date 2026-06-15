# UserManagement-IDaaS-Platform

A Multi-Tenant Identity-as-a-Service (IDaaS) platform built with FastAPI, SQLAlchemy, Alembic, and MySQL.

Planned integrations include Redis, JWT Authentication, SDKs, Admin Portal, and Enterprise Identity features.

---

# 🚀 Overview

UserManagement-IDaaS-Platform is a centralized identity and access management solution that allows organizations to integrate user management, authentication, authorization, and security features without building them from scratch.

Instead of implementing:

- User Registration
- Login & Authentication
- Password Reset
- User Profiles
- Roles & Permissions
- Session Management
- Audit Logging

for every application, organizations can integrate this platform through APIs or SDKs and focus on their core business.

---

# 🚧 Project Status

This project is currently under active development.

Current Phase:

✅ Foundation Setup

In Progress:

- Identity Data Models
- Authentication Framework
- RBAC Foundation

Planned:

- SDK Development
- Redis Integration
- Admin Portal
- Enterprise Identity Features

---

# Why This Project?

Most organizations spend significant engineering effort repeatedly building:

- User Registration
- Login Systems
- Role Management
- Permission Management
- Password Reset Flows
- Session Tracking

These features are necessary but rarely unique to the business.

This project aims to provide a reusable identity platform so organizations can focus on their actual business requirements instead of rebuilding identity infrastructure.

---

# 🎯 Problem Statement

Almost every application requires:

- User Management
- Authentication
- Authorization
- Security Controls

Teams repeatedly build the same identity system across projects.

This leads to:

- Increased development effort
- Higher maintenance costs
- Security vulnerabilities
- Inconsistent implementations

---

# 💡 Solution

This platform provides identity infrastructure as a service.

Applications integrate using APIs or SDKs while the platform handles:

- Identity Management
- Authentication
- Authorization
- Role-Based Access Control (RBAC)
- Session Management
- Audit Tracking
- Tenant Isolation

---

# 🧠 What is IDaaS?

IDaaS (Identity as a Service) is a cloud-based identity management model where authentication and user management are provided as a reusable service.

Examples include:

- Auth0
- Okta
- AWS Cognito
- Clerk
- Keycloak

This project aims to provide similar functionality using a modern FastAPI-based architecture.

---

# 🏢 Real-World Example

Imagine a Hospital Management System.

Without IDaaS:

The hospital must build:

- Login
- Registration
- Password Reset
- User Roles
- User Permissions

internally.

With IDaaS:

```python
from usermanagement_idaas import Client

client = Client(api_key="hospital_api_key")

client.create_user(...)
client.login(...)
client.assign_role(...)
```

The platform handles identity and security while the hospital focuses on healthcare workflows.

---

# 🏗️ High-Level Architecture

```text
Client Application
        |
        |
       SDK
        |
        |
FastAPI API Gateway
        |
Authentication Middleware
        |
Service Layer
        |
DAO Layer
        |
MySQL Database
```

---

# 🔄 Request Flow

Example: Create User

Step 1:

```python
client.create_user({
    "name": "John",
    "email": "john@example.com"
})
```

Step 2:

```http
POST /users
x-api-key: abc123
```

Step 3:

Middleware resolves:

```text
API Key → Organization
```

Step 4:

Service Layer:

- Validates request
- Applies business rules
- Checks permissions

Step 5:

DAO Layer:

```sql
INSERT INTO users (...)
```

Step 6:

Response:

```json
{
  "user_id": 1,
  "status": "created"
}
```

---

# 🏢 Multi-Tenant Architecture

This platform follows a Shared Database + Shared Schema approach.

Organizations are customers of the platform.

Users belong to organizations.

Example:

Organization A (Hospital)

Users:

- Doctor
- Nurse
- Receptionist

Organization B (School)

Users:

- Principal
- Teacher
- Student

Although both organizations share the same database and application instance, their data remains isolated using organization_id based tenant boundaries.

---

# 🔑 Tenant Isolation Strategy

Every business table contains:

```text
organization_id
```

Example:

| id | organization_id | name |
|----|-----------------|------|
| 1 | 100 | John |
| 2 | 200 | Mary |

All queries are scoped using:

```text
organization_id
```

to prevent data leakage between tenants.

---

# 📦 Core Features

## User Management

- Create User
- Update User
- Delete User
- User Profiles
- User Lifecycle Management

## Authentication

- Login
- Logout
- JWT Access Tokens
- Refresh Tokens
- Password Reset

## Authorization

- Roles
- Permissions
- RBAC

## Security

- Password Hashing
- Session Tracking
- Audit Logging
- Tenant Isolation

---

# 🗄️ Database Design

Core tables:

## organizations

Stores customer organizations.

```text
id
name
api_key
plan
status
created_at
updated_at
```

---

## users

Stores organization users.

```text
id
organization_id
email
phone
password_hash
is_active
is_verified
created_at
updated_at
```

---

## roles

Stores organization-specific roles.

Examples:

```text
Admin
Manager
Doctor
Teacher
```

---

## permissions

Stores available permissions.

Examples:

```text
create_user
delete_user
view_reports
```

---

## user_roles

Maps users to roles.

---

## role_permissions

Maps roles to permissions.

---

## refresh_tokens

Stores refresh token metadata.

---

## audit_logs

Stores security and activity logs.

---

# 🔐 Security Design

## Password Storage

Passwords are never stored in plain text.

Supported hashing algorithms:

- bcrypt
- Argon2

Example:

```text
$2b$12$xxxxxxxxxxxxxxxxxxxx
```

---

## Sensitive Data

Sensitive user information can be:

- Access Controlled
- Encrypted (future enhancement)

---

## API Security

Every request must include:

```http
x-api-key
```

The platform resolves:

```text
API Key → Organization
```

before processing requests.

---

## Authorization

RBAC is enforced through:

```text
User
↓
Role
↓
Permission
```

---

# ⚙️ Technology Stack

## Backend

- FastAPI

## Database

- MySQL

## ORM

- SQLAlchemy

## Migrations

- Alembic

## Caching

- Redis (Planned)

## Authentication

- JWT

## Deployment

- Docker (Planned)

---

# 📂 Project Structure

```text
app/
│
├── api/
│   └── routes/
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── middleware.py
│
├── dao/
│
├── db/
│
├── models/
│
├── schemas/
│
├── services/
│
└── main.py

docs/
│
├── API_SPEC.md
├── ARCHITECTURE.md
├── DATABASE.md
├── ROADMAP.md
└── VISION.md

migrations/
tests/
```

---

# 🛠️ Local Development Setup

## Prerequisites

Install:

- Python 3.11+
- MySQL 8+
- Git

Verify:

```bash
python --version
git --version
mysql --version
```

---

## Clone Repository

```bash
git clone <repository-url>
cd UserManagement-IDaaS-Platform
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Git Bash

```bash
source venv/Scripts/activate
```

PowerShell

```powershell
venv\Scripts\Activate.ps1
```

CMD

```cmd
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create:

```text
.env
```

Example:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=password
DB_NAME=user_management_idaas
```

---

## Create Database

```sql
CREATE DATABASE user_management_idaas;
```

---

## Run Migrations

```bash
alembic upgrade head
```

---

## Start FastAPI

```bash
uvicorn main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# 🔄 Development Workflow

## Create Migration

```bash
alembic revision --autogenerate -m "migration_name"
```

---

## Apply Migration

```bash
alembic upgrade head
```

---

## View Current Migration

```bash
alembic current
```

---

## View Migration History

```bash
alembic history
```

---

# 📈 Current Development Status

## Completed

- Project Structure
- FastAPI Setup
- SQLAlchemy Setup
- Alembic Setup
- MySQL Integration
- Environment Configuration
- Organization Model
- Initial Migration

## In Progress

- User Model
- Role Model
- Permission Model

## Planned

- Authentication Module
- RBAC Engine
- Redis Integration
- SDK Development
- Admin Portal

---

# 🗺️ Roadmap

Detailed roadmap available in:

```text
docs/ROADMAP.md
```

Additional documentation:

```text
docs/VISION.md
docs/ARCHITECTURE.md
docs/DATABASE.md
docs/API_SPEC.md
```

---

# 🎯 Long-Term Vision

Organizations should never need to rebuild:

- Registration
- Login
- Password Reset
- Role Management
- Permissions
- Session Tracking

Instead:

```text
SDK/API Integration
            ↓
UserManagement-IDaaS-Platform
            ↓
Identity Infrastructure Delivered as a Service
```

The goal is to provide a scalable, secure, and developer-friendly identity platform that organizations can integrate in minutes rather than spending weeks building authentication systems from scratch.