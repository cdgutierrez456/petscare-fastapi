from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Permission(Base):
    __tablename__ = "permissions"
    id_permission = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    route = Column(String)

    profiles = relationship("Profile", secondary="profile_permission", back_populates="permissions")