from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class Profile(Base):
    __tablename__ = "profiles"
    id_profile = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(String, ForeignKey("users.id_user", ondelete="CASCADE"))

    user = relationship("User", back_populates="profiles")
    permissions = relationship("Permission", secondary="profile_permission", back_populates="profiles")