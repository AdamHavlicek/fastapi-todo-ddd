"""
    Sql alchemy entities
"""
from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func


@as_declarative()
class Base(object):
    id_: Mapped[int] | int | None = Column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] | datetime | None = Column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] | datetime | None = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    is_deleted: Mapped[bool] | bool | None = Column(Boolean, default=False)
