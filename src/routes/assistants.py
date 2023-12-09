from fastapi import APIRouter

from src.utils.constants import client


assistant_router = APIRouter()

@assistant_router.get("/list/assistants")
def get_assistants():
    assistants = client.beta.assistants.list()
    return assistants

@assistant_router.post("/assistants")
def create_assistants():
    return {"Hello": "World"}
