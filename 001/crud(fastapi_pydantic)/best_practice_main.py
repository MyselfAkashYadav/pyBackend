#for best practice approach dont always put everything in main.py 

# create a folder routers and inside that create a file tasks.py

from routers import tasks

app.include_router(tasks.router,prefix="/tasks",tags=["Tasks"])
# now all routes defined in tasks.py will be prefixed with /tasks

# Explanation: This code snippet demonstrates how to organize FastAPI routes using routers for better modularity and maintainability.

# also we have depends in fastapi for dependency injection 

from fastapi import Depends

# simulate a DB connection session 
def get_db():
    db="Database Connection Session"
    try:
        yield db
    finally:
        print("Database Closed")
@app.get("/items/")
async def read_items(db=Depends(get_db)):
    # you can now use 'db' inside this function safely

    return {"db_status": "connected"} 

# 3. is env and etc..


