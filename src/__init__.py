from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from src.errors import register_all_errors
from .middleware import register_middleware

version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix = f"/api/{version}"

app = FastAPI(
    title = "Bookly",
    description = description,
    version = version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "email":"upadhyayaadi99@gmail.com"
    },
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)

register_middleware(app)


app.include_router(book_router, prefix = "/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix = "/api/{version}/auth", tags=['auth'])
app.include_router(review_router, prefix = "/api/{version}/reviews", tags=['reviews'])
app.include_router(tags_router, prefix="/api/{version}/tags", tags=['tags'])