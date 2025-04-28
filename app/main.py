from fastapi import FastAPI
from aplicacao.backend.app.api.endpoints import moldes 
from aplicacao.backend.app.database import create_db_and_tables 
from contextlib import asynccontextmanager 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
