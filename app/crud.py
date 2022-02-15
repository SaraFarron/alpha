from sqlalchemy.orm import Session
import models
import schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_product_by_name(db: Session, name: str):
    return db.query(models.Product).filter(models.Product.name == name).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


# def create_product(db: Session, product: schemas.ProductCreate):
#     fake_hashed_password = product.password + 'nothashed'
#     db_product = models.Product(email=product.email, hashed_password=fake_hashed_password)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product
