from fastapi import FastAPI

from src.routes import *


app = FastAPI()

app.include_router(assistant_router)
app.include_router(questions_router)
app.include_router(health_router)
