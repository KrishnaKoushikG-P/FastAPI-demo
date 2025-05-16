from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "Name": "abcd",
        "Age": 12,
        "Class": 7
    },
    2:{
        "Name": "efgh",
        "Age": 13,
        "Class": 8
    }
}

class Student(BaseModel):
    Name: str
    Age: int
    Class: int

@app.get('/')
def index():
    return {"name":"Data"}

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(description = "The student ID you want to see", gt=0, le=5)):
    return students[student_id]

@app.get('/get-by-name')
def get_by_name(name:Optional[str]=None):
    for student_id in students:
        if students[student_id]["Name"] == name:
            return students[student_id]
    return {"data":"not found"}

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"Error": "Student does not Exists"}

    students[student_id] = student
    return students[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exists"}
    del students[student_id]
    return {"Message":"Student deleted successfully"}

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app)