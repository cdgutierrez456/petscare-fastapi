from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class PetBase(BaseModel):
    event_name: str
    initial_date: datetime
    end_date: datetime
    speaker_name: str

class PetCreate(PetBase):
    pass

class PetOut(PetBase):
    id_pet: int
    state_id: int
    model_config = ConfigDict(from_attributes=True)