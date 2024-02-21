from app.model import DHTReading
from app.schema import DHTReadingSchema
from sqlalchemy.orm import Session


def create_dht_reading(db: Session, dht_reading: DHTReadingSchema):
    _dht_reading = DHTReading(
        humidity=dht_reading.humidity,
        temperature=dht_reading.temperature
    )
    db.add(_dht_reading)
    db.commit()
    db.refresh(_dht_reading)
    return _dht_reading
