from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get('/')
async def api_overview(): return {'success': 'indeed'}
