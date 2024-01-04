from environs import Env
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

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
SessionLocal = sessionmaker(autocommit=False, autflush=False, bind=engine)

def create_db():
    if database_exists(engine.url):
        print("Database exists!")
    else:
        print("Creating database...")
        create_database(engine.url)
        print("Database created!")