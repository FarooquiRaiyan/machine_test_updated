
from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(255), index = True)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key = True, index = True)
    product_name = Column(String(255), index = True)
    category_id = Column(Integer, ForeignKey("category.id"))
    
    