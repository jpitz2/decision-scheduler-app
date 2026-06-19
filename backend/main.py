from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Task
from schemas import TaskCreate


Base.metadata.create_all(bind=engine)

app = FastAPI()

# TODO: /tasks endpoints

@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(name=task.name, priority=task.priority, duration=task.duration, completion_status=task.completion_status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@app.get("/health")
def health_check():
    return {"status" : "ok"}

# Serves everything in /frontend at the root URL (e.g. localhost:8000/index.html)
app.mount("/frontend", StaticFiles(directory="../frontend", html=True), name="frontend")

