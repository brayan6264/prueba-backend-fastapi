# Mnages the database connection and session for the application
# This file sets up the database connection and initializes the ORM models
from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv
#Load environment variables from .env file
load_dotenv()  

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

# Gets a session for database operations
def get_session():
    with Session(engine) as session:
        yield session

# Initializes the tables in the database
def init_db():
    from app.models.user import User
    from app.models.product import Product
    from app.models.purchase import Purchase
    SQLModel.metadata.create_all(engine)