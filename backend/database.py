from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "Customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    country = Column(String)

class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class Order(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("Customers.id"))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    total = Column(Float)

class OrderItem(Base):
    __tablename__ = "OrderItems"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("Orders.id"))
    product_id = Column(Integer, ForeignKey("Products.id"))
    quantity = Column(Integer)

DATABASE_URL = "sqlite:///./sql_assistant.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
