from fastapi import FastAPI

from app import models
from app.infrastructure.database.postgres.database import engine
from app.features.task.presentation.routes import tasks
from app.features.user.presentation.routes.user_routes import user_router

app = FastAPI()
app.include_router(tasks.router)
app.include_router(user_router)


@app.on_event('startup')
def startup_event():
    models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
