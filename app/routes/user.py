from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db

router = APIRouter()

@router.get("/me", response_model='')
async def me(db: AsyncSession = Depends(get_db)):
    return ''
  
@router.get("/list")
async def list_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return ''

@router.get("/{user_id}")
async def get_user(user_id: int = Path(..., description="ID del usuario"), db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información del usuario {user_id}"}

@router.put("/{user_id}")
async def update_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Usuario {user_id} actualizado"}

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Usuario {user_id} eliminado"}

  