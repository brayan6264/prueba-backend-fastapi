from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead
from app.db.database import get_session
from app.services.user_service import create_user
from app.schemas.user import UserLogin
from app.services.user_service import authenticate_user
from app.utils.jwt_handler import create_access_token
from fastapi.responses import JSONResponse
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserUpdate
from app.services.user_service import update_user, delete_user
from fastapi import Body

router = APIRouter()
# Endpoint for user registration
@router.post("/", response_model=UserRead, status_code=201)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    new_user = create_user(user, session)
    return new_user
# Endpoint for user login
@router.post("/login")
def login_user(data: UserLogin, session: Session = Depends(get_session)):
    user = authenticate_user(data.email, data.password, session)
    token = create_access_token({"sub": str(user.user_id)})
    return JSONResponse(content={"access_token": token, "token_type": "bearer","user_id": str(user.user_id)})


@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserRead)
def update_me(
    data: UserUpdate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return update_user(current_user, data, session, partial=True)

@router.delete("/me", status_code=204)
def delete_me(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    delete_user(current_user, session)
    return