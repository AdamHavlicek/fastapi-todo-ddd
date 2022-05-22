from fastapi import Depends, status, HTTPException

from features.task.presentation.routes import router
from features.task.dependencies import get_tasks_use_case
from features.task.domain.entities.task_query_model import TaskReadModel
from features.task.domain.usecases.get_tasks import GetTasksUseCase
from features.task.presentation.schemas.task_error_message import ErrorMessageTasksNotFound


@router.get(
    '/',
    response_model=list[TaskReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageTasksNotFound
        }
    }
)
def get_tasks(
    skip: int = 0,
    limit: int = 100,
    get_tasks_use_case_: GetTasksUseCase = Depends(get_tasks_use_case)
):
    try:
        tasks = get_tasks_use_case_()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return tasks
