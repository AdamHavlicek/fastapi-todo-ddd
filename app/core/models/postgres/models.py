"""
    Sql alchemy entities
"""
from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.sql import func


@as_declarative()
class Base(object):
    id_: Column | int = Column(Integer, primary_key=True, index=True)
    created_at: Column | datetime = Column(TIMESTAMP, server_default=func.now())
    updated_at: Column | datetime = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    is_deleted: Column | bool = Column(Boolean, default=False)
