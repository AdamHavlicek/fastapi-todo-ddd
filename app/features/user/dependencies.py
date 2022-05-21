from fastapi import Depends
from sqlalchemy.orm import Session

from app.features.user.data.repositories.user_command_unit_of_work_impl import UserCommandUnitOfWorkImpl
from app.features.user.data.repositories.user_repository_impl import UserRepositoryImpl
from app.features.user.data.services.user_service_impl import UserQueryServiceImpl
from app.features.user.domain.repositories.user_repository import UserRepository
from app.features.user.domain.usecases.user_command_unit_of_work import UserCommandUnitOfWork
from app.features.user.domain.usecases.user_command_usecase import UserCommandUseCase, UserCommandUseCaseImpl
from app.features.user.domain.usecases.user_query_service import UserQueryService
from app.features.user.domain.usecases.user_query_usecase import UserQueryUseCase, UserQueryUseCaseImpl
from app.infrastructure.database.postgres.database import get_session


def user_query_use_case(session: Session = Depends(get_session)) -> UserQueryUseCase:
    user_query_service: UserQueryService = UserQueryServiceImpl(session)

    return UserQueryUseCaseImpl(user_query_service)


def user_command_use_case(session: Session = Depends(get_session)) -> UserCommandUseCase:
    # TODO: DI user repository and unity of work
    user_repository: UserRepository = UserRepositoryImpl(session)

    unit_of_work: UserCommandUnitOfWork = UserCommandUnitOfWorkImpl(
        session,
        user_repository
    )

    return UserCommandUseCaseImpl(unit_of_work)
