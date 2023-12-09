from fastapi import FastAPI

from src.routes import assistant_router


app = FastAPI()

app.add_api_route(assistant_router)
