# pydantic is not just for fast api ; it is for data validation. In professional backends,never trust the user input or data coming from outside the system. Pydantic enforces types.

#  its kind of like typescript for python.

from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List

# these imports explanation BaseModel library from pydantic is used to create data models with type validation. Field is used to provide additional metadata and validation rules for model fields. EmailStr is a specialized type that ensures a string is a valid email address.
# Optional and List are imported from the typing module to specify optional fields and list types in the data models.

# 1 Define the Schema(the shape or structure of the data)

class User(BaseModel):
    username:str
    #Field is used to provide additional validation and metadata for the age field.(min & max val etc..)
    age:int=Field(gt=0,lt=100,description="Age must be between 1 and 99")
    email:str
    is_active:bool=True
    skills:List[str]=[]

#2 Simulating Incoming "Bad" Dara (like from a frontend)

external_data={
    "username":"arch_user",
    "age":25,
    "email":"user@example.com",
    "skills":["python","linux"]
}

#3 Data Validation and Parsing
try:
    user=User(**external_data)
    print("SUCCESS:")
    print(user.model_dump()) #convert back from pydantic model to dictionary
    print("user email:",user.email)
except Exception as e:
    print("ERROR:",e)

