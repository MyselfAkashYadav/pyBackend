# simple to-do application using FastAPI and Pydantic

from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from typing import List,Optional 
from uuid import UUID,uuid4

app=FastAPI()

# ---- SCHEMAS (pydantic models) ----

# 1. base schema (shared attributes or properties)


#  we are creating a class TaskBase that inherits from BaseModel. This class defines the common attributes for a task, including title, description, and completed status.
class TaskBase(BaseModel):
    title:str
    description:Optional[str]=None
    completed:bool=False

# 2. create schema (what the user sends when creating a new task)

# here we create a TaskCreate class that inherits from TaskBase. This class is used when a user wants to create a new task. It doesn't add any new attributes but serves as a distinct schema for task creation. pass is used because we don't need to add any additional fields or methods; we just want to use the structure defined in TaskBase.
class TaskCreate(TaskBase):
    pass

# 3. response schema (what we return - includes id)
# here UUID is used to uniquely identify each task. The TaskResponse class inherits from TaskBase and adds an id attribute of type UUID. This schema is used when returning task data to the client, ensuring that each task has a unique identifier along with the other attributes defined in TaskBase.
class TaskResponse(TaskBase):
    id:UUID

# ---- FAKE DATABASE-----
# here we simulate a database with an in-memory list to store tasks. TaskResponse objects will be stored in this list as they are created.
# whats will happen is in beginning tasks_db is an empty list. As tasks are created using the API, TaskResponse objects (which include a unique id) will be added to this list, simulating the behavior of a database.
tasks_db:List[TaskResponse]=[]

# ---Routes----

# GET all tasks

@app.get("/tasks",response_model=List[TaskResponse])
async def get_tasks():
    return tasks_db

# POST create a new task

@app.post("/tasks",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
async def create_task(task:TaskCreate):
    new_task=TaskResponse(id=uuid4(),**task.model_dump())
    tasks_db.append(new_task)
    return new_task

# GET single task

@app.get("/tasks/{task_id}",response_model=TaskResponse)
async def get_task(task_id:UUID):
    # Find task
    task=next((t for t in tasks_db if t.id==task_id),None)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task 

# put (update)  task

@app.put("/tasks/{task_id}",response_model=TaskResponse)
async def update_task(task_id:UUID,updated_task:TaskCreate):
    for i,t in enumerate(task_id):
        if t.id==task_id:
            #create new task object keepint the old ID but new data 
            tasks_db[i]=TaskResponse(id=task_id,**updated_task.model_dump())
            return tasks_db[i]
    raise HTTPException(status_code=404,detail="Task not found")
# delete task
@app.delete("/tasks/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id:UUID):
    for i,t in enumerate(tasks_db):
        if t.id==task_id:
            del tasks_db[i]
            return
    raise HTTPException(status_code=404,detail="Task not found")

# In this code, we have defined a simple to-do application using FastAPI and Pydantic. The application allows users to create, read, update, and delete tasks. Each task has a title, description, completed status, and a unique identifier (UUID). The tasks are stored in an in-memory list that simulates a database. The API endpoints handle various operations on the tasks, ensuring data validation and proper response formatting using Pydantic models.