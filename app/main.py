from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.background_jobs import schedule_jobs
from app.config import create_db, engine
from app.model import Base
from app.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating DB")
    create_db()
    Base.metadata.create_all(bind=engine)
    
    print("scheduling cron jobs")
    schedule_jobs()
    yield

app = FastAPI(lifespan=lifespan)


@app.get('/')
async def root():
    return "Home"

app.include_router(router, prefix="/dht_reading", tags=["dht_reading"])
