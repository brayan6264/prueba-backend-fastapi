from pydantic import BaseModel, EmailStr, constr
from typing import Optional

# Create new user schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8) #type: ignore

# Return user without password
class UserRead(BaseModel):
    user_id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[constr(min_length=8)] = None #type: ignore