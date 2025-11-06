from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db


from app.schemas.auth import AuthBase

router = APIRouter()

@router.post("/login")
async def login(auth: AuthBase, db: AsyncSession = Depends(get_db)):
    return await auth_crud.authenticate_user(db, auth)

@router.post("/register")
async def register(register, db):
    return ''