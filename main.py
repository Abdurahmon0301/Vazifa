from typing import Optional
from fastapi import FastAPI, status
from pydantic import BaseModel, Field
app = FastAPI()

students = [
    {"id": 1, "name": "Student 1", "fan":[
        {"name":"matematika", "baxo":"A"},
        {"name":"adabiyot", "baxo":"B"},
        {"name":"kimyo", "baxo":"F"},
        {"name":"fizika", "baxo":"C"},
        {"name":"biologiya", "baxo":"D"},
    ]},
    {"id": 2, "name": "Student 2", "fan":[
        {"name":"matematika", "baxo":"A"},
        {"name":"adabiyot", "baxo":"B"},
        {"name":"kimyo", "baxo":"F"},
        {"name":"fizika", "baxo":"C"},
        {"name":"biologiya", "baxo":"D"},
    ]},
    {"id": 3, "name": "Student 3", "fan":[
        {"name":"matematika", "baxo":"A"},
        {"name":"adabiyot", "baxo":"B"},
        {"name":"kimyo", "baxo":"F"},
        {"name":"fizika", "baxo":"C"},
        {"name":"biologiya", "baxo":"D"},
    ]},
    {"id": 4, "name": "Student 4", "fan":[
        {"name":"matematika", "baxo":"A"},
        {"name":"adabiyot", "baxo":"B"},
        {"name":"kimyo", "baxo":"F"},
        {"name":"fizika", "baxo":"C"},
        {"name":"biologiya", "baxo":"D"},
    ]},
    {"id": 5, "name": "Student 5", "fan":[
        {"name":"matematika", "baxo":"A"},
        {"name":"adabiyot", "baxo":"B"},
        {"name":"kimyo", "baxo":"F"},
        {"name":"fizika", "baxo":"C"},
        {"name":"biologiya", "baxo":"D"},
    ]},
    
]

books = [
    {"id": 1, "title": "Python", "author": "Kimdir", "comment":["hello", "hi"], "status": True},
    {"id": 2, "title": "Backend", "author": "Kimdir", "comment":["hello", "hi"], "status": False},
    {"id": 3, "title": "Backend", "author": "Kimdir", "comment":["hello", "hi"], "status": True},
    {"id": 4, "title": "Backend", "author": "Kimdir", "comment":["hello", "hi"], "status": False},
    {"id": 5, "title": "Backend", "author": "Kimdir", "comment":["hello", "hi"], "status": True}
]

class User(BaseModel):
    name: str
    info: str
    price: int

@app.get("/books" , status_code=status.HTTP_200_OK)
async def get_books(limit: int = 5):
    result = []

    if limit > len(books):
        return{f"size":len(books),"result":books}
    for i in range(limit):

        result.append(books[i])

    return{f"size":len(result), "result": result}

@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    return {"error": "Book not found"}, status.HTTP_404_NOT_FOUND

@app.post("/book/id/{id}/title/{title}", status_code=status.HTTP_200_OK)
async def update_book(id: int, name: str, author: str):
    for book in books:
        if book["id"] == id:
            book["title"] = name
            book["author"] = author
            return book
    return {'error': "Book is not updated"}

@app.delete("/book/{id}")
async def delete_book(id: int):
    for i, book in enumerate(books):
        if book["id"] == id:
            books.pop(i)
    return None

@app.post("/book/id/{id}/title/{title}/author/{author}", status_code=status.HTTP_200_OK)
async def create_bookk(id: int, name: str, author: str):
    for book in books:
        book["id"] = id
        book["title"] = name
        book["author"] = author
        return  



@app.get("/student/{stident_id}")
async def get_student_id(id: int):
    for student in students:
        if student["id"] == id:
            return student["id"]

@app.get("/student/{stident_id}/grandles/{subject}")
async def get_student(id: int, subject: str):
    for student in students:
        if student["id"] == id:
            for fan in student["fan"]:
                if fan["name"] == subject:
                    return {
                            "id": student["id"],
                            "Ismi": student["name"],
                            "Fan": fan["name"],
                            "Baxo": fan["baxo"]
                        }
                

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(max_length=20)
    year: int = Field(ge=1600, le=2030)
    isbn: Optional[int]
    pages: Optional[int]


@app.post("/book_create")
async def create_book(book: Book):
    return {"message": f"{book.title} nomli kitob yaratildi!", "book": book}


class Contact(BaseModel):
    phone: int
    email: str
    adress: str

class Student(BaseModel):
    name: str
    age: int
    contact: Contact

@app.post("/student_create")
async def create_student(student: Student):
    return {"message": f"Student with name {student.name} created!", "student": student}

