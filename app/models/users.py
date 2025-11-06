from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id_user = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    fullname = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    state_id = Column(Integer, default=True)

    state = relationship("State", back_populates="state")
    pets = relationship("Pet", back_populates="owner")
    profiles = relationship("Profile", back_populates="user")
    roles = relationship("UserGlobalRole", back_populates="user")
    clinics = relationship("ClinicMember", back_populates="user")