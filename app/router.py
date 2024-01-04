from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from app import crud
from app.schema import DHTReadingSchema, RequestDHTReading, Response

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/dht_reading')
async def create(request: RequestDHTReading, db: Session=Depends(get_db)):
    crud.create_dht_reading(db, request.parameter)
    return Response(code=200, status="OK")