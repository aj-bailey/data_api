from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class DHTReadingSchema(BaseModel):
    humidity: float
    temperature: float

    class Config:
        orm_mode = True

class RequestDHTReading(BaseModel):
    parameter: DHTReadingSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    response: Optional[T]
