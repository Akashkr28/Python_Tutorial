from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class Blog(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  # Optional field with default value None

cart_date = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3}
}

cart = Cart(**cart_date)