from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 Main St",
    city="Jamshedpur",
    postal_code="831017",
)

user = User(
    id=1,
    name="Akash",
    address=address,
)

user_data = {
    "id": 1,
    "name": "Akash",
    "address": {
        "street": "123 Main St",
        "city": "Jamshedpur",
        "postal_code": "831017",
    }
}

user = User(**user_data)
print(user)