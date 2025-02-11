from fastapi import APIRouter, HTTPException

from api.routes import books

api_router = APIRouter()

api_router.include_router(books.router, prefix="/books", tags=["books"])

@api_router.get("/books/{book_id}")
async def get_book(book_id: int):

#     """Retrieve a book by its ID."""
#     #books = api_router.get(book_id)
 
    if books is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return books