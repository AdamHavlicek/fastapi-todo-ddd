from fastapi import Depends, HTTPException, status

from core.error.user_exception import UserAlreadyExistsError
from features.user.dependencies import get_create_user_use_case
from features.user.domain.entities.user_command_model import UserCreateModel
from features.user.domain.entities.user_query_model import UserReadModel
from features.user.domain.usecases.create_user import CreateUserUseCase
from features.user.presentation.routes import router
from features.user.presentation.schemas.user_error_message import ErrorMessageUserAlreadyExists


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
def create_user(data: UserCreateModel, create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case)):
    try:
        user = create_user_use_case(data)
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
