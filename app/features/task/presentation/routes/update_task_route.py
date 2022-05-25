from fastapi import Depends, HTTPException, status

from app.core.error.task_exception import TaskNotFoundError
from app.features.task.dependencies import get_update_task_use_case
from app.features.task.domain.entities.task_command_model import TaskUpdateModel
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.usecases.update_task import UpdateTaskUseCase
from app.features.task.presentation.routes import router
from app.features.task.presentation.schemas.task_error_message import ErrorMessageTaskNotFound


@router.put(
    '/{id_}/',
    response_model=TaskReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageTaskNotFound
        }
    }
)
async def update_task(
    id_: int,
    data: TaskUpdateModel,
    update_task_use_case: UpdateTaskUseCase = Depends(get_update_task_use_case)
):
    try:
        user = update_task_use_case((id_, data))
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user
