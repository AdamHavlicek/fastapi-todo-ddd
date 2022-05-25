
from fastapi import Depends, HTTPException, status

from app.core.error.user_exception import UserNotFoundError
from app.features.user.dependencies import get_user_use_case
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.usecases.get_user import GetUserUseCase
from app.features.user.presentation.routes import router
from app.features.user.presentation.schemas.user_error_message import ErrorMessageUserNotFound


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
):
    try:
        user = get_user_use_case_((id_, ))
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user
