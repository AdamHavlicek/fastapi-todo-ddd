from fastapi import FastAPI

from app import models
from app.infrastructure.database.postgres.database import engine
from app.features.task.presentation.routers import tasks
from app.features.user.presentation.routers import users

app = FastAPI()
app.include_router(tasks.router)
app.include_router(users.router)


@app.on_event('startup')
def startup_event():
    models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
