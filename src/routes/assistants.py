from fastapi import APIRouter, UploadFile

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import AssistantListResponse, AssistantResponse
from src.services.assistants import *
from src.utils.constants import client, logging


assistant_router = APIRouter(
    prefix="/api/v1/assistant",
    tags=["Assistant"],
    responses=ErrorResponses.all(),
)

@assistant_router.get(
    "/list",
    response_model=AssistantListResponse().model(),
    response_description=AssistantListResponse().get("description"),
)
def list_assistants():
    try:
        assistants = get_assistant_list()
        return AssistantListResponse().format(assistants)
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}

@assistant_router.get(
        "/{assistant_id}",
        response_model=AssistantResponse().model(),
        response_description=AssistantResponse().get("description"),
    )
def get_assistants(assistant_id: str):
    try:
        assistant = get_assistant(assistant_id)
        return AssistantResponse().format(assistant)
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}

@assistant_router.post("/")
def create_assistants(file: UploadFile):
    try:
        create_assistant(file.filename)
        return {"message": "Succeeded"}
    except FileNotFoundError as e:
        logging.error(f"File \"{file.filename}\" does not exist")
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}

@assistant_router.post("/chapters")
def create_multiple_assistant(file: UploadFile, chapters: str):
    try:
        create_assistant(file.filename)
        return {"message": "Succeeded"}
    except FileNotFoundError as e:
        logging.error(f"File \"{file.filename}\" does not exist")
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}
