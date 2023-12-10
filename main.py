from fastapi import FastAPI

from src.routes import *


app = FastAPI()

app.include_router(assistant_router)
app.include_router(user_router)
app.include_router(thread_router)
app.include_router(health_router)
