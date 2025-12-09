from fastapi import FastAPI

app=FastAPI()

# the simplest GET request

@app.get('/')
async def root():
    return {"message":"Hello Arch User"}

# Path Parameters (e.g., /items/5)
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    # FastAPI automatically converts item_id to int and validates it.
    # if user sends "abc", FastAPI sends a 422 Error automatically.
    return {"item_id":item_id}

# Query Parameters (e.g., /items/?q=somequery)
@app.get("/search")
async def search(q: str ="default"):
    return {"query":q}
