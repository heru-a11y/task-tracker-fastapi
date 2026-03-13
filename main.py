from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import database_models
import models
from database import session, engine

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks", response_model=list[models.Task])
def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(database_models.Task).all()

@app.post("/tasks", response_model=models.Task)
def create_task(task: models.TaskCreate, db: Session = Depends(get_db)):
    db_task = database_models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/{task_id}", response_model=models.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(database_models.Task).filter(database_models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=models.Task)
def update_task(task_id: int, updated_task: models.TaskBase, db: Session = Depends(get_db)):
    task = db.query(database_models.Task).filter(database_models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.query(database_models.Task).filter(database_models.Task.id == task_id).update({
        database_models.Task.title: updated_task.title,
        database_models.Task.description: updated_task.description,
        database_models.Task.completed: updated_task.completed
    })
    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(database_models.Task).filter(database_models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}