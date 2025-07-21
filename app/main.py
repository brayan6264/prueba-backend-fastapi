from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import init_db
from app.api import user
from app.api import product
from app.api import purchase

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init the database when the app starts
    init_db()
    yield
    # Optional code to run when the app shuts down (e.g., close resources)

app = FastAPI(
    title="Prueba Técnica Auxiliar de Programación",
    version="1.0.0",
    lifespan=lifespan
)
# Include routers for user, product and purchase APIs
app.include_router(user.router, prefix="/api/users", tags=["Usuarios"])
app.include_router(product.router, prefix="/api/products", tags=["Productos"])
app.include_router(purchase.router, prefix="/api/purchases", tags=["Compras"])