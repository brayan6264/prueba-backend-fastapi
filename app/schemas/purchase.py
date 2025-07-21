from pydantic import BaseModel
from typing import List
class PurchaseCreate(BaseModel):
    product_id: int
    total_products: int

class PurchaseRead(BaseModel):
    id_purchase: int
    product_name: str
    total_products: int

    class Config:
        orm_mode = True