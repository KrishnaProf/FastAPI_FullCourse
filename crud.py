from fastapi.exceptions import HTTPException
from fastapi import FastAPI, status
from model import Book, BookUpdate

app = FastAPI()
books = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coethol",
        "publish_date": "1988-02-01"
    },
    {
        "id": 2,
        "title": "The God of Small things",
        "author": "Paulo Gaur",
        "publish_date": "1989-02-01"
    },
    {
        "id": 3,
        "title": "The White Tiger",
        "author": "Naga Coethol",
        "publish_date": "1985-02-01"
    },
    {
        "id": 4,
        "title": "The Dairy",
        "author": "Paulo hello",
        "publish_date": "1988-09-01"
    }
]

@app.get("/books")
def get_books():
    return books

@app.get("/book/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")

@app.post("/createbook")
def create_book(book : Book):
    new_book = book.model_dump()
    books.append(new_book)
    return books

@app.put("/book/{book_id}")
def updteBook(book_id: int, book_update: BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publish_date'] = book_update.publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not found")