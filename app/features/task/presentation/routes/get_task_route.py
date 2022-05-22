from fastapi import Depends, status, HTTPException

from core.error.task_exception import TaskNotFoundError
from features.task.dependencies import get_task_use_case
from features.task.domain.entities.task_query_model import TaskReadModel
from features.task.domain.usecases.get_task import GetTaskUseCase
from features.task.presentation.routes import router
from features.task.presentation.schemas.task_error_message import ErrorMessageTaskNotFound


@router.get(
    '/{id_}/',
    response_model=TaskReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageTaskNotFound
        }
    }
)
def get_task(
    id_: int,
    get_task_use_case_: GetTaskUseCase = Depends(get_task_use_case)
):
    try:
        task = get_task_use_case_(id_)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return task
