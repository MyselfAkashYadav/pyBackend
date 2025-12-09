# explanation : This code defines a FastAPI router for handling task-related endpoints. It imports the APIRouter class from FastAPI, creates a router instance, and defines a GET endpoint at "/tasks" that returns a simple JSON message indicating a list of tasks. This modular approach allows for better organization of routes in larger applications.



from fastapi import APIRouter
router=APIRouter()

# so the browser will see end point as http://localhost:8000/tasks/ 
@router.get("/")
async def get_tasks():
    return {"message":"List of tasks"}

