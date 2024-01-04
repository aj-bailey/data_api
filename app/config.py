from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgresql:postgres@localhost:5432/dht_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autflush=False, bind=engine)
Base = declarative_base()
