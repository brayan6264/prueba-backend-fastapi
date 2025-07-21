from sqlmodel import Session
from app.models.purchase import Purchase
from app.schemas.purchase import PurchaseCreate
from app.models.user import User
from app.models.product import Product
from fastapi import HTTPException
from sqlmodel import select, col
from app.models.product import Product
from typing import List
from app.schemas.purchase import PurchaseRead


def create_purchase(data: PurchaseCreate, user: User, session: Session) -> Purchase:
    product = session.get(Product, data.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    purchase = Purchase(
        user_id=user.user_id,
        product_id=data.product_id,
        total_products=data.total_products
    )
    session.add(purchase)
    session.commit()
    session.refresh(purchase)
    return purchase

def get_purchases_by_user(user: User, session: Session) -> List[PurchaseRead]:
    statement = (
        select(Purchase.id_purchase, Product.name.label("product_name"), Purchase.total_products)
        .join(Product, Purchase.product_id == Product.product_id)
        .where(Purchase.user_id == user.user_id)
    )
    results = session.exec(statement).all()
    return [PurchaseRead(**row._mapping) for row in results]