from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/login")
async def login(auth, db):
    return ''
  
@router.post("/register")
async def register(register, db):
    return ''