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

# In this example, we define a User model with fields for username, age, email, is_active, and skills. We then simulate incoming data from an external source and use Pydantic to validate and parse that data into a User instance. If the data is valid, we print the user information; otherwise, we catch and print any validation errors.
# 4 Testing with Invalid Data
invalid_data={
    "username":"arch_user",
    "age":150,  # Invalid age
    "email":"not-an-email",
    "skills":["python","linux"]
}
try:
    user=User(**invalid_data)
    print("SUCCESS:")
    print(user.model_dump())
except Exception as e:
    print("ERROR:",e)
# In this case, the age is out of the specified range and the email is not valid, so Pydantic will raise validation errors, which we catch and print.
# Overall, Pydantic provides a powerful way to ensure data integrity and consistency in Python applications
# Example Output:
# SUCCESS:
# {'username': 'arch_user', 'age': 25, 'email': 'user
#@example.com', 'is_active': True, 'skills': ['python', 'linux']}
# user email:
#
# worong example output:
# ERROR: 1 validation error for User
# age
#   ensure this value is less than 100 (type=value_error.number.not_lt; limit_value=100)
# email
#   value is not a valid email address (type=value_error.email)@example.com"
# is_active: True
# skills: ['python', 'linux']
