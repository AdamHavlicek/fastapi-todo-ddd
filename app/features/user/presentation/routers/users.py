"""
    User Api Router
"""
from fastapi import Depends, HTTPException, status

from app.features.task.presentation.routers import router
from app.features.user.dependencies import user_query_use_case, user_command_use_case
from app.features.user.domain.usecases.user_command_model import UserCreateModel
from app.features.user.domain.usecases.user_command_usecase import UserCommandUseCase
from app.features.user.domain.usecases.user_query_model import UserReadModel
from app.features.user.domain.usecases.user_query_usecase import UserQueryUseCase
from app.core.error.user_exception import UserAlreadyExistsError
from app.features.user.presentation.schemas.user_error_message import (
    ErrorMessageUserAlreadyExists,
    ErrorMessageUsersNotFound,
)


@router.post(
    '/',
    response_model=UserReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'model': ErrorMessageUserAlreadyExists
        }
    }
)
def create_user(data: UserCreateModel, user_command_use_case_: UserCommandUseCase = Depends(user_command_use_case)):
    try:
        user = user_command_use_case_.create_user(data)
    except UserAlreadyExistsError as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exception.message
        )
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user


@router.get(
    '/',
    response_model=list[UserReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageUsersNotFound
        }
    }
)
def get_users(skip: int = 0, limit: int = 100, user_query_use_case_: UserQueryUseCase = Depends(user_query_use_case)):
    try:
        users = user_query_use_case_.fetch_users()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return users


# @router.post('/{user_id}/tasks', response_model=schemas.task.Task)
# def create_task_for_user(
#         user_id: int,
#         item: schemas.task.TaskCreate,
#         db: Session = Depends(get_session)
# ):
#     return crud.task.create_user_task(db, item, user_id)
