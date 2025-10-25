# Book Service API (Backend)

A FastAPI backend service for book management with JWT authentication, reviews, and tagging system.

## Quick Start with Docker

- Clone the repository:
    * git clone https://github.com/AadarshU210/Fastapi_Bookly
    * cd Fastapi_Bookly
- Run with Docker Compose:
    * docker-compose up --build
- Access the API documentation:
    * http://localhost:8000/api/v1/docs

 The database migrations run automatically on startup.

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
- PostgreSQL
- Pydantic (Data validation)
- JWT (Authentication)
