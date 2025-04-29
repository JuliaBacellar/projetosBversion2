# crud.py
from models import Molde  # Importa o modelo de dados
from schemas import MoldeCreate, MoldeUpdate  # Importa os schemas (DTOs)
from sqlalchemy.orm import Session

# Buscar todos os moldes
def get_all_moldes(db: Session):
    return db.query(Molde).all()

# Buscar molde por ID
def get_molde_by_id(db: Session, molde_id: int):
    return db.query(Molde).filter(Molde.id == molde_id).first()

# Criar novo molde
def create_molde(db: Session, molde: MoldeCreate):
    db_molde = Molde(
        nome=molde.nome,
        prateleira=molde.prateleira,
        status_presenca=molde.status_presenca,
        qr_code=molde.qr_code,
    )
    db.add(db_molde)
    db.commit()
    db.refresh(db_molde)
    return db_molde

# Atualizar molde existente
def update_molde(db: Session, molde_id: int, molde_update: MoldeUpdate):
    db_molde = get_molde_by_id(db, molde_id)
    if not db_molde:
        return None
    for key, value in molde_update.dict(exclude_unset=True).items():
        setattr(db_molde, key, value)
    db.commit()
    db.refresh(db_molde)
    return db_molde

# Deletar molde
def delete_molde(db: Session, molde_id: int):
    db_molde = get_molde_by_id(db, molde_id)
    if not db_molde:
        return None
    db.delete(db_molde)
    db.commit()
    return db_molde


