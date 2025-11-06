from sqlalchemy import ForeignKey, Column, String, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class UserGlobalRole(Base):
    __tablename__ = "user_global_roles"
    
    user_id = Column(String, ForeignKey('users.id_user'))
    role_id = Column(String, ForeignKey('roles.id_rol'))
    
    __table_args__ = {
        PrimaryKeyConstraint('user_id', 'role_id')
    }
    
    user = relationship("User", back_populates="global_roles")
    role = relationship("Role", back_populates="user_assignments")