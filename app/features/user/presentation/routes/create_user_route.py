from fastapi import Depends, HTTPException, status, Response, Request

from app.core.error.user_exception import UserAlreadyExistsError
from app.features.user.dependencies import get_create_user_use_case
from app.features.user.domain.entities.user_command_model import UserCreateModel
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.usecases.create_user import CreateUserUseCase
from app.features.user.presentation.routes import router
from app.features.user.presentation.schemas.user_error_message import ErrorMessageUserAlreadyExists


@router.post(
    '/',
    response_model=UserReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'model': ErrorMessageUserAlreadyExists
        }
    },
)
def create_user(
    data: UserCreateModel,
    response: Response,
    request: Request,
    create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case),
):
    try:
        user = create_user_use_case((data, ))
    except UserAlreadyExistsError as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exception.message
        )
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    response.headers['location'] = f"{request.url.path}{user.id_}"
    return user
