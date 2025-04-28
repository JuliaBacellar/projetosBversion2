from fastapi import APIRouter, Depends
from aplicacao.backend.app.crud import get_moldes, upsert_molde
from aplicacao.backend.app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/moldes")
def read_moldes(db: Session = Depends(get_db)):
    return get_moldes(db)

@router.put("/moldes/{model_id}")
def update_molde(model_id: int,  n_ferramental: str, part_number: str, qrcode_number: str):
    return upsert_molde(model_id, n_ferramental,part_number,qrcode_number)