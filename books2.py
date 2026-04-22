from fastapi import FastAPI,Body,Path

from pydantic import BaseModel,Field

from typing import Optional

app=FastAPI()




class Book:
    id:int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id :Optional[int] = Field( default=None,description="ID is not needed on create")
    author:str=Field(min_length=1)
    title:str=Field(min_length=3)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=-1,lt=5)
    published_date:int
    
    
    model_config={
        
        "json_schema_extra":{
            "example":{
                "title":"A new BOOK",
                "author":"coding with yoni",
                "description":"a new descritpion  of a book",
                
                
            }
        }
        
    }
    
    
    

    
    
    

    
    
    

    


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 2, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 2, 2026)
]




@app.get("/books")

async  def read_all_books():
    
    return  BOOKS



@app.post("/create_boook")

async  def create_book(book_request:BookRequest):
    new_book=Book(**book_request.model_dump())
    
    BOOKS.append(find_book_id(new_book))
    



def  find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id=BOOKS[-1].id+1
        
    else :
        book.id=1
        
    return book
    



@app.get("/books/{book_id}")

async def read_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
        
        



@app.get("/books")

async def read_by_rating(book_rating:int):
    books_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            books_return.append(book)
            
            
@app.put("/books/update")
async  def update_book(book:BookRequest):
    
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
            
            



