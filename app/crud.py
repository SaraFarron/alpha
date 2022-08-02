from sqlalchemy.orm import Session
from fastapi import HTTPException

import models


def get_all(db: Session, model: models.Base):
    return db.query(model).all()


def get_concrete(db: Session, model: models.Base, hallmark: dict, many: bool = False):
    result = db.query(model).filter_by(**hallmark)
    if not result:
        raise HTTPException(404, 'Object not found')
    return result.all() if many else result.first()

def create_entry(db: Session, model: models.Base, data: dict):
    db_model = model(**data)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

def update_entry(db: Session, model: models.Base, model_id, data: dict):
    """
    Partial update
    """
    db_model = get_concrete(db, model, {'id': model_id})
    for k, v in data.items():
        if v:
            setattr(db_model, k, v)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def delete_entry(db: Session, model: models.Base, model_id: int):
    db_model = get_concrete(db, model, {'id': model_id})
    if not db_model:
        raise HTTPException(404, detail=f'{model.__class__.__name__} with id {model_id} was not found')
    db.delete(db_model)
    db.commit()
    return
