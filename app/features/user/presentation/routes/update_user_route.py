from fastapi import Depends, HTTPException, status

from app.core.error.user_exception import UserNotFoundError
from app.features.user.dependencies import get_update_user_use_case
from app.features.user.domain.entities.user_command_model import UserUpdateModel
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.usecases.update_user import UpdateUserUseCase
from app.features.user.presentation.routes import router
from app.features.user.presentation.schemas.user_error_message import ErrorMessageUserNotFound


@router.patch(
    '/{id_}/',
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageUserNotFound
        }
    }
)
async def update_user(
    id_: int,
    data: UserUpdateModel,
    update_user_use_case: UpdateUserUseCase = Depends(get_update_user_use_case)
):
    try:
        user = update_user_use_case((id_, data))
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user
