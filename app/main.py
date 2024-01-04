from app.model import Base

from app.config import engine
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy_utils import database_exists, create_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    if database_exists(engine.url):
        print("Database exists!")
    else:
        print("Creating database...")
        create_database(engine.url)
        print("Database created!")
        
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/')
async def Home():
    print(database_exists(engine.url))
    return database_exists(engine.url)
