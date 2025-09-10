from sqlalchemy import Column, String, DateTime
from datetime import datetime, timezone

class User(Base):
    __tablename__ = 'users'
    
    id_user = Column(
        String, 
        primary_key=True,
        autoincrement=False
    )
    name_user = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

