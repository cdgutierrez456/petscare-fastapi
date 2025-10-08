from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime, timezone
from app.database import Base

class Clinic(Base):
    __tablename__ = 'clinics'
    
    id_clinic = Column(String, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    created_by = Column(String, ForeignKey('users.id_user'))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))