from fastapi import HTTPException, Depends, status

from app.core.error.task_exception import TaskNotFoundError
from app.features.task.dependencies import get_delete_task_use_case
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.usecases.delete_task import DeleteTaskUseCase
from app.features.task.presentation.routes import router
from app.features.task.presentation.schemas.task_error_message import ErrorMessageTaskNotFound


@router.delete(
    '/{id_}/',
    response_model=TaskReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageTaskNotFound
        }
    }
)
def delete_task(
    id_: int,
    delete_task_use_case: DeleteTaskUseCase = Depends(get_delete_task_use_case)
):
    try:
        task = delete_task_use_case((id_, ))
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return task
