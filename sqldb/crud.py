from sqlalchemy.orm import Session
from . import models, schemas
# import csv
# import datetime

# def get_all_predictions(db: Session, skip: int = 0, limit: int = 10000):
#     return db.query(models.Product).offset(skip).limit(limit).all()

def get_all_entities(db : Session):
    return db.query(models.Entities).all()

def get_all_categories(db : Session):
    return db.query(models.Categories).all()

def get_all_products(db : Session):
    return db.query(models.Products).all()

def get_category_by_id(db : Session, id: int):
    return db.query(models.Categories).filter(models.Categories.id == id).all()

def get_product_by_id(db : Session, id: int):
    return db.query(models.Products).filter(models.Products.id == id).all()
