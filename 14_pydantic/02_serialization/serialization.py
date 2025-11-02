from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    steet: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')}
    )

user = User(
    id=1,
    name="John Doe",
    email="B2A2y@example.com",
    created_at=datetime(2024, 6, 1, 12, 0, 0),
    address=Address(
        steet="123 Main St",
        city="Anytown",
        zip_code="12345"
    ),
    is_active=False,
    tags=["Premium", "Subscriber"]
)

python_dict = user.model_dump()
print(python_dict)

json_str = user.model_dump_json()
print(json_str)