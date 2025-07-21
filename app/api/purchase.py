from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.database import get_session
from app.schemas.purchase import PurchaseCreate
from app.services.purchase_service import create_purchase
from app.models.purchase import Purchase
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.purchase import PurchaseRead
from typing import List
from app.services.purchase_service import get_purchases_by_user

router = APIRouter()

@router.post("/", response_model=Purchase, status_code=201)
def make_purchase(
    data: PurchaseCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return create_purchase(data, current_user, session)

@router.get("/me", response_model=List[PurchaseRead])
def my_purchases(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return get_purchases_by_user(current_user, session)