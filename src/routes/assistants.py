from fastapi import APIRouter, UploadFile

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import AssistantListResponse, AssistantCreatedResponse, AssistantResponse
from src.services.assistants import *
from src.utils.constants import logging
from src.utils.pdf_spliter import split_into_chapters


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

@assistant_router.post(
        "/",
        response_model=AssistantCreatedResponse().model(),
        response_description=AssistantCreatedResponse().get("description"),
    )
def create_assistants(file: UploadFile):
    try:
        assistant = create_assistant(file)
        return AssistantCreatedResponse().format(assistant)
    except FileNotFoundError as e:
        logging.error(f"File \"{file.filename}\" does not exist")
    except Exception as e:
        logging.error(f"{str(e)}")

@assistant_router.post("/chapters")
def create_multiple_assistant(file: UploadFile, chapters: str):
    try:
        chapters = split_into_chapters(file, chapters)
        for chapter in chapters:
            create_assistant(chapter)
    except FileNotFoundError as e:
        logging.error(f"File \"{file.filename}\" does not exist")
    except Exception as e:
        logging.error(f"{str(e)}")
