import uuid
from typing import Any,List 
from aplicacao.backend.app.models import Molde
from aplicacao.backend.app.database import engine 
from sqlmodel import Session, select
from fastapi import FastAPI

app = FastAPI()

def get_moldes() -> List[Molde]:
    with Session(engine) as session:
        statement = select(Molde)
        results = session.exec(statement).all()
        return results

def upsert_molde(model_id: int, n_ferramental: str, part_number: str, qrcode_number: str)-> Molde:
    with Session(engine) as session:
        molde = session.get(Molde, model_id)
        if molde:
            molde.n_ferramental = n_ferramental,
            molde.part_number = part_number,
            molde.qrcode_number = qrcode_number
        else:
            molde = Molde(
                id=model_id,
                n_ferramental=n_ferramental,
                part_number=part_number,
                qrcode_number=qrcode_number 
            )
            session.add(molde)
        session.commit()
        session.refresh(molde)
        return molde


