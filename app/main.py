from app.config import create_db, engine
from app.model import Base
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/')
async def root():
    return "Home"

app.include_router(router, prefix="/dht_reading", tags=["dht_reading"])