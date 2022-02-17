from sqlalchemy.orm import Session
from database import Base
import schemas


def get_instance(db: Session, instance: Base, instance_id: int):
    return db.query(instance).filter(instance.id == instance_id).first()


def get_all(db: Session, instance: Base, skip: int = 0, limit: int = 100):
    return db.query(instance).offset(skip).limit(limit).all()


# def create_instance(db: Session, product: schemas.ProductCreate, instance: Base):
#     fake_hashed_password = product.password + 'nothashed'
#     db_product = instance(email=product.email, hashed_password=fake_hashed_password)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product
