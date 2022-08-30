from sqlalchemy import Integer, ForeignKey, String, Column, Boolean, DateTime, Float
from .database import Base
from sqlalchemy.orm import relationship
# import datetime

class Entities(Base):
    __tablename__ = "Entities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    stockings_to_entities = relationship("Stockings", back_populates = "entities_to_stockings")

class Stockings(Base):
    __tablename__ = "Stockings"
    id = Column(Integer, primary_key=True, index=True)
    EntityId = Column(Integer, ForeignKey("Entities.id"))

    entities_to_stockings = relationship("Entities", back_populates = "stockings_to_entities")
    products_to_stockings = relationship("Products", back_populates = "stockings_to_products")

class Categories(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    categories_to_product = relationship("Products")

class Products(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, index=True)
    CategorieId = Column(Integer, ForeignKey("Categories.id"))
    name = Column(String)
    quantity_unit = Column(String)
    price = Column(Float)
    pricePerLiterOrKg = Column(Float)
    lifetime = Column(Integer)
    StockingId = Column(Integer, ForeignKey("Stockings.id"))
    stock_min = Column(Float)
    stock_max = Column(Float)
    quantity = Column(Float)
    # "margin" could be great

    stockings_to_products = relationship("Stockings", back_populates="products_to_stockings")
    sells_to_products = relationship("ProductSells", back_populates="products_to_sells")
    trashes_to_products = relationship("Trashes", back_populates="products_to_trashes")

class DaySells(Base):
    __tablename__= "DaySells"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    # date = Column(String, default=datetime.date.today().strftime("%d%m%Y"))
    # find a way to transform date in : dayoftheweek, dayofthemonth, monthoftheyear, publicholidays, season

    day_to_sells = relationship("ProductSells")

class ProductSells(Base):
    __tablename__ = "ProductSells"
    id = Column(Integer, primary_key=True, index=True)
    DaySellId = Column(Integer, ForeignKey("DaySells.id"))
    ProductId = Column(Integer, ForeignKey("Products.id"))
    quantity = Column(Float)
    # "discount" could be great

    products_to_sells = relationship("Products", back_populates="sells_to_products")


class Trashes(Base):
    __tablename__ = "Trashes"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    rehabilitate = Column(Boolean, default=False)
    gift = Column(Boolean, default=False)
    ProductId = Column(Integer, ForeignKey("Products.id"))
    quantity = Column(Float)
    dateProd = Column(DateTime)

    products_to_trashes = relationship("Products", back_populates="trashes_to_products")