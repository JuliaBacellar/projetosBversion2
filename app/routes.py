from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas

router = APIRouter(
    prefix="/moldes",
    tags=["moldes"]
)

@router.get("/", response_model=list[schemas.MoldeResponse])
def get_moldes(db: Session = Depends(get_db)):
    return crud.get_all_moldes(db)

@router.get("/{molde_id}", response_model=schemas.MoldeResponse)
def get_molde(molde_id: int, db: Session = Depends(get_db)):
    molde = crud.get_molde_by_id(db, molde_id)
    if not molde:
        raise HTTPException(status_code=404, detail="Molde não encontrado")
    return molde

@router.post("/", response_model=schemas.MoldeResponse)
def create_molde(molde: schemas.MoldeCreate, db: Session = Depends(get_db)):
    return crud.create_molde(db, molde)

@router.put("/{molde_id}", response_model=schemas.MoldeResponse)
def update_molde(molde_id: int, molde_update: schemas.MoldeUpdate, db: Session = Depends(get_db)):
    molde = crud.update_molde(db, molde_id, molde_update)
    if not molde:
        raise HTTPException(status_code=404, detail="Molde não encontrado para atualizar")
    return molde

@router.delete("/{molde_id}")
def delete_molde(molde_id: int, db: Session = Depends(get_db)):
    molde = crud.delete_molde(db, molde_id)
    if not molde:
        raise HTTPException(status_code=404, detail="Molde não encontrado para deletar")
    return {"ok": True}


##exemplo requisição para a raspberry 

# @router.post("/sensor/update")
# def update_status_sensor(qr_code: str, status_presenca: bool, db: Session = Depends(get_db)):
#     molde = db.query(crud.Molde).filter(crud.Molde.qr_code == qr_code).first()
#     if not molde:
#         raise HTTPException(status_code=404, detail="Molde com QR code não encontrado")
#     molde.status_presenca = status_presenca
#     db.commit()
#     db.refresh(molde)
#     return {"message": "Status do molde atualizado com sucesso"}
