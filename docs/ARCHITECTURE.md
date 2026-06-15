# Architecture

## High-Level Flow

Client Application
↓
SDK
↓
API Gateway (FastAPI)
↓
Authentication Middleware
↓
Service Layer
↓
DAO Layer
↓
MySQL

---

## Tenant Resolution

Each request contains:

x-api-key

The middleware resolves:

api_key → organization_id

All operations are scoped to the organization.

---

## Multi-Tenant Strategy

Shared Database

organizations
users
roles
permissions

Each table contains:

organization_id

for tenant isolation.

---

## Future Components

- Redis
- Rate Limiting
- Background Jobs
- Email Service
- Notification Service
- SDKs