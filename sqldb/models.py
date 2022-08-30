from sqlalchemy import Integer, ForeignKey, String, Column, Boolean, DateTime, Float
from .database import Base
from sqlalchemy.orm import relationship
# import datetime

# class Season(Base):
#     __tablename__ = "season"
#     id = Column(Integer, primary_key=True, index=True)
#     spring = Column(Boolean, default=False)
#     summer = Column(Boolean, default=False)
#     autumn= Column(Boolean, default=False)
#     winter = Column(Boolean, default=False)

#     season_to_product = relationship("product")
#     season_to_sells = relationship("sells")

# class Product(Base):
#     __tablename__ = "product"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     category = Column(String)
#     season_id = Column(Integer, ForeignKey("season.id"))
#     price = Column(Float)
#     margin = Column(Float)
#     stock = Column(Float)
#     stock_min = Column(Float)
#     stock_max = Column(Float)
#     lifetime = Column(Integer)

#     sells_to_product = relationship("ProductSells", back_populates="product_to_sells")
#     trash_to_product = relationship("Trash", back_populates="product_to_trash")

# class Sells(Base):
#     __tablename__ = "sells"
#     id = Column(Integer, primary_key=True, index=True)
#     product_id = Column(Integer, ForeignKey("product.id"))
#     quantity = Column(Float)
#     discount = Column(Float)
#     season_id = Column(Integer, ForeignKey("season.id"))
#     dayofweek = Column(String)
#     monthofsell = Column(Integer)
#     dayofsell = Column(Integer)
#     yearofsell = Column(Integer)
#     publicholiday = Column(Boolean, default=False)

#     product_to_sells = relationship("Product", back_populates="sells_to_product")
#     season_to_sells = relationship("Season", back_populates="sells_to_season")
#     sells_to_store = relationship("Store")

# class Store(Base):
#     __tablename__ = "store"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     sells_id = Column(Integer, ForeignKey("sells.id"))

# class Trash(Base):
#     __tablename__ = "trash"
#     id = Column(Integer, primary_key=True, index=True)
#     product_id = Column(Integer, ForeignKey("product.id"))
#     # date = Column(String, default=datetime.date.today().strftime("%d%m%Y"))
#     date_sell = Column(DateTime)
#     date_prod = Column(DateTime)
#     quantity = Column(Float)
#     rehabilitate = Column(Boolean, default=False)
#     gift = Column(Boolean, default=False)

#     product_to_trash = relationship("Product", back_populates="trash_to_product")