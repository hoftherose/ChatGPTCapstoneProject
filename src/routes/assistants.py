from fastapi import APIRouter, UploadFile

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import AssistantListResponse, AssistantCreatedResponse, AssistantResponse
from src.utils.constants import logging
from src.services.assistants import *


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
    assistants = get_assistant_list()
    return AssistantListResponse().format(assistants)

@assistant_router.get(
        "/{assistant_id}",
        response_model=AssistantResponse().model(),
        response_description=AssistantResponse().get("description"),
    )
def get_assistants(assistant_id: str):
    assistant = get_assistant(assistant_id)
    return AssistantResponse().format(assistant)

@assistant_router.post(
        "/",
        response_model=AssistantCreatedResponse().model(),
        response_description=AssistantCreatedResponse().get("description"),
    )
def create_assistants(file: UploadFile):
        assistant = create_assistant(file)
        return AssistantCreatedResponse().format(assistant)
