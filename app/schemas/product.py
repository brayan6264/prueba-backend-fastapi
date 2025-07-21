from pydantic import BaseModel
from typing import Optional
# Schemas for product operations
class ProductCreate(BaseModel):
    name: str
    price: float
    url_image: str

class ProductRead(BaseModel):
    product_id: int
    name: str
    price: float
    url_image: str

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    url_image: Optional[str] = None

