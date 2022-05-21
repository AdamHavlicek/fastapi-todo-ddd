"""
    Pydantic Schema models
"""
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id_: int
    owner_id: int

    class Config(object):
        orm_mode = True
