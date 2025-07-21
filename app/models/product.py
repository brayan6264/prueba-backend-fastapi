# ORM model for product management
# This model is used to represent a product in the database
from sqlmodel import SQLModel, Field
from typing import Optional
# Object Relational Mapping (ORM) model for product management
class Product(SQLModel, table=True):
    product_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    url_image: str