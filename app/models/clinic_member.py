from sqlalchemy import Column, PrimaryKeyConstraint, String, ForeignKey, DateTime, Integer
from datetime import datetime, timezone

class ClinicMember(Base):
    __tablename__ = 'clinic_members'
    
    clinic_id = Column(String, ForeignKey('clinics.id_clinic'))
    user_id = Column(String, ForeignKey('users.id_user'))
    role_id = Column(Integer, ForeignKey('roles.id_role'))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    __table_args__ = {
        PrimaryKeyConstraint('clinic_id', 'user_id')
    }