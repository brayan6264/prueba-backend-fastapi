# ORM model for purchase management
# This model is used to represent a purchase in the database
from sqlmodel import SQLModel, Field
from typing import Optional
# Object Relational Mapping (ORM) model for purchase management
class Purchase(SQLModel, table=True):
    id_purchase: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    product_id: int = Field(foreign_key="product.product_id")
    total_products: int