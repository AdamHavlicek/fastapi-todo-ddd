from fastapi import Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.features.task.presentation.routes import router
from app.infrastructure.database.postgres.database import get_session


@router.get('/', response_model=list[schemas.task.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return crud.task.get_tasks(db, skip, limit)
