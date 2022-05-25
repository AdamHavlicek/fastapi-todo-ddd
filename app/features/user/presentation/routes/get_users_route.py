from fastapi import Depends, HTTPException, status

from app.features.user.dependencies import get_users_use_case
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.usecases.get_users import GetUsersUseCase
from app.features.user.presentation.routes import router
from app.features.user.presentation.schemas.user_error_message import ErrorMessageUsersNotFound


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
def get_users(skip: int = 0, limit: int = 100, get_users_use_case_: GetUsersUseCase = Depends(get_users_use_case)):
    try:
        users = get_users_use_case_(None)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return users
