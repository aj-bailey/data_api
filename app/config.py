from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from environs import Env
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from scripts.prev_date_to_csv import prev_date_to_csv
from scripts.upload_csv_data import upload_prev_date_data


env = Env()
env.read_env(".env")

DATABASE_URL = URL.create(
        drivername="postgresql+psycopg2",
        username=env.str("POSTGRES_USER"),
        password=env.str("POSTGRES_PASSWORD"),
        host=env.str("DATABASE_HOST"),
        port=env.str("PORT"),
        database=env.str("POSTGRES_DB"),
    ).render_as_string(hide_password=False)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db():
    if database_exists(engine.url):
        print("Database exists!")
    else:
        print("Creating database...")
        create_database(engine.url)
        print("Database created!")

def schedule_jobs():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(prev_date_to_csv, CronTrigger(hour=0, minute=15))
    print("Added prev_date_to_csv to run daily at 00:15")

    scheduler.add_job(upload_prev_date_data, CronTrigger(hour=0, minute=20))
    print("Added upload_prev_date_data to run daily at 00:30")
    
    scheduler.start()
