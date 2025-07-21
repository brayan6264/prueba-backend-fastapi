#ORM model for user management
# This model is used to represent a user in the database
from sqlmodel import SQLModel, Field
from typing import Optional
#Object Relational Mapping (ORM) model for user management
class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str  