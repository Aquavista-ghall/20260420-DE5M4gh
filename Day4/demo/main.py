#print("Hello World")

#Get a user to give you their dob and return their age on the 11/05/2039
# from datetime import datetime as dt
# dob = input()
# target = '11-05-1991 00:00:00'
# dobdate = dt.strptime(dob, '%d%m%Y')

# print(dobdate)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data Model
class Book(BaseModel):
    id: int
    title: str
    author: str

#Fake DB
books: List[Book] = [
    Book(id=1, title="bookname 1", author="nirosh"),
    Book(id=2, title="booktitle 2", author="Unknown")
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the library api"}

# Getting all books - Endpoint
@app.get("/books", response_model=List[Book])
def get_books():
    return books

#Write an endpoint that takes a book ID and returns the specific book
@app.get("/books/{book_id}", response_model=Book)
def get_book_by_id_v2(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error":"book not found"}