from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class DHTReadingSchema(BaseModel):
    humidity: float
    temperature: float

    class Config:
        orm_mode = True

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    response: Optional[T]