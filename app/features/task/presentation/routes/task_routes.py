"""
    task router
    https://github.com/tiangolo/fastapi/issues/2916#issuecomment-818260637
"""
from app.features.task.presentation.routes.delete_task_route import delete_task
from app.features.task.presentation.routes.update_task_route import update_task
from app.features.task.presentation.routes.create_task_route import create_task
from app.features.task.presentation.routes.get_task_route import get_task
from app.features.task.presentation.routes.get_tasks_route import get_tasks, router

task_router = router
