from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime
#class modelo de moldes,prateleiras
class MoldeBase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    n_ferramental : str = Field(max_length=20)
    part_number : str = Field(max_length=25)
    qrcode_number : str = Field(min_length=7 , max_length=10)


class Molde(MoldeBase, table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    data_criacao:datetime = Field(default_factory=datetime.utcnow)