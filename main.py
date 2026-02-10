from fastapi import FastAPI
from typing import Optional

from model import Student

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def greet(name : str, age : Optional[int] = None):
    return {"message": f"Hello {name} and your age is {age}"}

@app.post("/create_student")
def create_student(student : Student):
    return {
        "name" : student.name,
        "age" : student.age,
        "roll": student.roll

    }
    