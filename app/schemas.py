from datetime import datetime 
from typing import Optional
from pydantic import BaseModel

class MoldeCreate(BaseModel):
    n_ferramental: str
    part_number : str 
    qrcode_number: str

class MoldeRead(MoldeCreate):
    id:int
    data_criacao: datetime  