from sqlalchemy import Column, Integer, String, Enum

class Role(Base):
    __tablename__ = 'roles'
    
    id_role = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    scope = Column(Enum('global', 'clinic'))