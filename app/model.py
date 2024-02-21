from datetime import datetime

from sqlalchemy import BIGINT, FLOAT, TIMESTAMP, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column
from typing_extensions import Annotated

INT_PK = Annotated[
    int,
    mapped_column(
        Integer, primary_key=True
    )
]


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now()
    )


class TableNameMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"


class DHTReading(Base, TableNameMixin, TimestampMixin):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    humidity: Mapped[float] = mapped_column(FLOAT)
    temperature: Mapped[float] = mapped_column(FLOAT)
