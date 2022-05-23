"""
    user router
    https://github.com/tiangolo/fastapi/issues/2916#issuecomment-818260637
"""
from app.features.user.presentation.routes.create_user_route import create_user
from app.features.user.presentation.routes.delete_user_route import delete_user
from app.features.user.presentation.routes.get_user_route import get_user
from app.features.user.presentation.routes.get_users_route import get_users
from app.features.user.presentation.routes.update_user_route import update_user, router

user_router = router