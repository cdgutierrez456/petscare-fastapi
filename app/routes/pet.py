from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.pet import PetCreate

from app.database import get_db

router = APIRouter()

@router.get("/list")
async def list_mascotas(db: AsyncSession = Depends(get_db)):
    return {"msg": "Lista de todas las mascotas (admin)"}

@router.get("/{mascota_id}")
async def get_mascota(mascota_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Información de la mascota {mascota_id}"}

@router.post("/", response_model=PetCreate)
async def create_mascota(db: AsyncSession = Depends(get_db)):
    return {"msg": "Mascota registrada correctamente"}

@router.put("/{mascota_id}")
async def update_mascota(mascota_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Mascota {mascota_id} actualizada"}

@router.delete("/{mascota_id}")
async def delete_mascota(mascota_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Mascota {mascota_id} eliminada"}

@router.put("/{mascota_id}/asignar-doctor/{doctor_id}")
async def assign_doctor_to_mascota(mascota_id: int, doctor_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Doctor {doctor_id} asignado a mascota {mascota_id}"}

@router.get("/{mascota_id}/historial")
async def get_historial_mascota(mascota_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Historial médico de la mascota {mascota_id}"}

@router.get("/{mascota_id}/eventos")
async def get_eventos_mascota(mascota_id: int, db: AsyncSession = Depends(get_db)):
    return {"msg": f"Eventos programados para la mascota {mascota_id}"}