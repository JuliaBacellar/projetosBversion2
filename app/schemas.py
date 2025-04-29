
from pydantic import BaseModel


class MoldeCreate(BaseModel):
    nome: str
    prateleira: str
    status_presenca: bool
    qr_code: str


class MoldeUpdate(BaseModel):
    nome: str | None = None
    prateleira: str | None = None
    status_presenca: bool | None = None
    qr_code: str | None = None


class MoldeResponse(BaseModel): #resposta da api depois de criar atualizar etc
    id: int
    nome: str
    prateleira: str
    status_presenca: bool
    qr_code: str

    class Config:
        orm_mode = True
