from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.pet import router as pet_router
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router
from .database import create_tables
import app.models

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(pet_router, prefix="/api/pets", tags=["Pets"])
app.include_router(user_router, prefix="/api/user", tags=["Users"])

@app.on_event("startup")
async def on_startup():
    await create_tables()

@app.get("/")
def read_root():
    return {"API": "PetsCare"}

