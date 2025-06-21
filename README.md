# Book Service API (Backend)

A FastAPI backend service for book management with JWT authentication, reviews, and tagging system.

## Features

- **User Authentication**
  - JWT-based authentication
  - User registration and login
  - Protected routes for authenticated users

- **Book Management**
  - Create, Read, Update, Delete books
  - Search books by title/author
  - Basic CRUD operations

- **Reviews System**
  - Authenticated users can write reviews
  - View all reviews for a book
  - Manage own reviews

- **Tagging System**
  - Add/remove tags to books
  - Filter books by tags

## Technologies

- Python 3.9+
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL/SQLite
- Pydantic (Data validation)
- JWT (Authentication)
