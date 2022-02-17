from fastapi import APIRouter, Depends
from crud import get_all, get_instance
from models import Batch, Product
from database import SessionLocal

router = APIRouter(
    responses={404: {'description': 'Not Found'}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/close-shift')
async def close_shift(shift_id: int, db: Depends(get_db)):
    pass


@router.get('/receive-batch')
async def receive_batch(batch_id: int, db: Depends(get_db)):
    batch = get_instance(db, Batch, batch_id)


@router.get('/products')
async def get_products(db: Depends(get_db)):
    products = get_all(db, Product)
    return products


@router.get('/batches')
async def get_batches():
    pass


@router.get('/tanks')
async def get_tanks():
    pass


@router.get('/suppliers')
async def get_suppliers():
    pass


@router.get('/employees')
async def get_employees():
    pass


@router.get('/trades')
async def get_trades():
    pass


@router.get('/shift')
async def get_shift():
    pass


@router.post('/new-trade')
async def create_trade(total: float):
    pass


@router.delete('/delete-trade')
async def delete_trade(trade_id: int):
    pass


@router.post('/generate-new-trade')
async def generate_new_trade():
    pass
