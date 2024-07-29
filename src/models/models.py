from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    my_products: List[Products]
    my_sales: List[Request]
    my_request: List[Request]

class Product(BaseModel):
    id: Optional[str] = None
    user: User
    name: str
    detail: str
    price: float
    status: bool = False

class Request(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int
    delivery: bool = False
    address: str
    comments: Optional[str] = None

