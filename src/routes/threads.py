from fastapi import APIRouter

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import ThreadListResponse
from src.services.threads import *
from src.utils.constants import logging


thread_router = APIRouter(
    prefix="/api/v1/thread",
    tags=["Threads"],
    responses=ErrorResponses.all(),
)

@thread_router.get(
    "/list/{thread_id}",
    response_model=ThreadListResponse().model(),
    response_description=ThreadListResponse().get("description"),
)
def list_threads():
    try:
        threads = get_thread_list()
        return ThreadListResponse().format(threads)
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}

@thread_router.get(
    "/list/{thread_id}",
    response_model=ThreadListResponse().model(),
    response_description=ThreadListResponse().get("description"),
)
def list_threads():
    try:
        threads = get_thread_list()
        return ThreadListResponse().format(threads)
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}
