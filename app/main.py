from contextlib import asynccontextmanager

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI

from app.config import create_db, engine
from app.model import Base
from app.router import router
from scripts.upload_csv_data import upload_prev_date_data

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating DB")
    create_db()
    Base.metadata.create_all(bind=engine)
    
    scheduler.add_job(upload_prev_date_data, CronTrigger(hour=16, minute=15))
    scheduler.start()
    yield

app = FastAPI(lifespan=lifespan)


@app.get('/')
async def root():
    return "Home"

app.include_router(router, prefix="/dht_reading", tags=["dht_reading"])
