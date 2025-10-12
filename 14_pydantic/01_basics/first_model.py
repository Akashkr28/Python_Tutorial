from pydantic import BaseModel # Importing BaseModel from Pydantic

class User(BaseModel): # Defining a User model that inherits from BaseModel
    id: int
    name: str
    is_active: bool

input_data = {'id': 101, 'name': "Chaicode", 'is_active': True}

user = User(**input_data)
print(user)