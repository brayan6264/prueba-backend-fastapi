from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password
from fastapi import HTTPException
from app.utils.security import verify_password
from app.utils.security import hash_password
from app.schemas.user import UserUpdate


# Service to handle user-related operations
# create a new user
def create_user(user_data: UserCreate, session: Session) -> User:
    # Check if the user already exists
    existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado.")

    # Hash the password
    hashed_pwd = hash_password(user_data.password)

    # Create and save the new user
    new_user = User(name=user_data.name, email=user_data.email, password=hashed_pwd)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

# Authenticate user by email and password
def authenticate_user(email: str, password: str, session: Session) -> User:
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta.")

    return user

def update_user(user: User, data: UserUpdate, session: Session, partial: bool = False) -> User:
    update_data = data.model_dump(exclude_unset=partial)

    if "name" in update_data:
        user.name = update_data["name"]
    if "email" in update_data:
        user.email = update_data["email"]
    if "password" in update_data:
        user.password = hash_password(update_data["password"])

    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(user: User, session: Session):
    session.delete(user)
    session.commit()