from fastapi import FastAPI

from src.routes import assistant_router


app = FastAPI()

app.include_router(assistant_router, prefix="/assistants")
