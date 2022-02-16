from fastapi import APIRouter

router = APIRouter(
    responses={404: {'description': 'Not Found'}},
)


@router.post('/close-shift')
async def close_shift(shift_id: int):
    pass


@router.get('/receive-batch')
async def receive_batch(batch_id: int):
    pass


@router.get('/products')
async def get_products():
    pass


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
