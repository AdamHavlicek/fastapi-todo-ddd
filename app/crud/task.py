from sqlalchemy.orm import Session
from sqlalchemy import select

from app import schemas
from app.features.task.data.models.task import Task


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    query = select(Task).offset(skip).limit(limit)

    return db.execute(query).all()


def create_user_task(db: Session, item: schemas.task.TaskCreate, user_id: int):
    db_item = Task(**item.dict(), owner_id=user_id)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
