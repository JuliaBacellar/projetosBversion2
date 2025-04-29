from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Molde(Base):
    __tablename__ = "moldes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    prateleira = Column(String, nullable=False)
    status_presenca = Column(Boolean, default=True) 
    qr_code = Column(String, unique=True, nullable=False)
