from fastapi import status, Depends, HTTPException

from features.task.dependencies import get_create_task_use_case
from features.task.domain.entities.task_command_model import TaskCreateModel
from features.task.domain.entities.task_query_model import TaskReadModel
from features.task.domain.usecases.create_task import CreateTaskUseCase
from features.task.presentation.routes import router


@router.post(
    '/',
    response_model=TaskReadModel,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    data: TaskCreateModel,
    create_task_use_case: CreateTaskUseCase = Depends(get_create_task_use_case)
):
    try:
        task = create_task_use_case(data)
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return task
