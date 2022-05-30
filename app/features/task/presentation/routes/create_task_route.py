from fastapi import status, Depends, HTTPException, Response, Request

from app.features.task.dependencies import get_create_task_use_case
from app.features.task.domain.entities.task_command_model import TaskCreateModel
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.usecases.create_task import CreateTaskUseCase
from app.features.task.presentation.routes import router


@router.post(
    '/',
    response_model=TaskReadModel,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    data: TaskCreateModel,
    response: Response,
    request: Request,
    create_task_use_case: CreateTaskUseCase = Depends(get_create_task_use_case)
):
    try:
        task = create_task_use_case((data, ))
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    response.headers['location'] = f"{request.url.path}{task.id_}"
    return task
