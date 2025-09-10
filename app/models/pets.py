from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

# from app.database import Base

class Pet():
    __tablename__ = 'pets'

    # ShortID-0001...
    id_pet = Column(String, primary_key=True, autoincrement=False)
    pet_name = Column(String, nullable=False)
    owner = Column(String, ForeignKey('users.id_user'))
    race_id = Column(Integer, ForeignKey('races.id_race'))
    species_id = Column(Integer, ForeignKey('species.id_specie'))

    # Relaciones
    state = relationship("State", back_populates="pets")
    race = relationship("Race", back_populates="pets")