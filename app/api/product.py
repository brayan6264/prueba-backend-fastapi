from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.database import get_session
from app.schemas.product import ProductCreate, ProductRead
from app.services.product_service import create_product, get_all_products, get_product_by_id, delete_product
from typing import List
from app.schemas.product import ProductUpdate
from app.services.product_service import update_product
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()
# Product routes for creating, retrieving, and deleting products
@router.post("/", response_model=ProductRead, status_code=201)
def create(
    data: ProductCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)  # protects the route with authentication
):
    return create_product(data, session)

@router.get("/", response_model=List[ProductRead])
def get_all(session: Session = Depends(get_session)):
    return get_all_products(session)

@router.get("/{product_id}", response_model=ProductRead)
def get_by_id(product_id: int, session: Session = Depends(get_session)):
    return get_product_by_id(product_id, session)

@router.delete("/{product_id}", status_code=204)
def delete(
    product_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)  # protects the route with authentication
):
    delete_product(product_id, session)
    return

@router.put("/{product_id}", response_model=ProductRead)
def update(
    product_id: int,
    data: ProductUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)  # protects the route with authentication
):
    return update_product(product_id, data, session)