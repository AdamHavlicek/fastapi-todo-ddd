from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models import Base


class Task(Base):
    """
        Task DTO is an object associated with user entity
    """
    __tablename__ = 'tasks'

    title: Column | str = Column(String, index=True)
    is_completed: Column | bool = Column(Boolean, default=False)
    owner_id: Column | int = Column(Integer, ForeignKey('users.id_'))

    owner = relationship('User', back_populates='tasks')
