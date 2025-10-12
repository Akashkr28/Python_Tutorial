from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # Ellipsis indicates that this field is required
        min_length=3, # Minimum length of 3 characters
        max_length=50, # Maximum length of 50 characters
        description="Employee Name", # Description of the field
        examples="Akash Kumar Singh" # Example value for the field
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000, # Greater than or equal to 10000
        description="Employee Salary",
        examples=100000.00
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r'''^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$''', # Regex for validating email format
    )
    phone: str = Field(..., regex=r'')
    age: int = Field(
        ...,
        ge=0,
        le=120,
        description="Age of the user",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=50,
        description="Discount percentage",
    )
                       