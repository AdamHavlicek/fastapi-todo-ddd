
from fastapi import Depends, HTTPException, status

from features.user.dependencies import get_user_use_case
from features.user.domain.entities.user_query_model import UserReadModel
from features.user.domain.usecases.get_user import GetUserUseCase
from features.user.presentation.routes import router
from features.user.presentation.schemas.user_error_message import ErrorMessageUserNotFound


@router.get(
    '/{id_}/',
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageUserNotFound
        }
    }
)
def get_user(
    id_: int,
    get_user_use_case_: GetUserUseCase = Depends(get_user_use_case)
) -> UserReadModel:
    try:
        user = get_user_use_case_(id_)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return user
