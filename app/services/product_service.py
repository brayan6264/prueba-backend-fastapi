from sqlmodel import Session, select
from app.models.product import Product
from app.schemas.product import ProductCreate
from fastapi import HTTPException
from app.schemas.product import ProductUpdate
# Service for managing product operations
# Create a new product
def create_product(data: ProductCreate, session: Session) -> Product:
    new_product = Product(**data.dict())
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product
# Get all products
def get_all_products(session: Session) -> list[Product]:
    return session.exec(select(Product)).all()
# Get a product by ID
def get_product_by_id(product_id: int, session: Session) -> Product:
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product
# Update a product
def delete_product(product_id: int, session: Session):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    session.delete(product)
    session.commit()

def update_product(product_id: int, data: ProductUpdate, session: Session) -> Product:
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)
    return product
