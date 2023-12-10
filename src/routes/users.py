from fastapi import APIRouter

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import UserListResponse
from src.services.users import *
from src.utils.constants import logging


user_router = APIRouter(
    prefix="/api/v1/user",
    tags=["User"],
    responses=ErrorResponses.all(),
)

@user_router.get(
    "/list",
    response_model=UserListResponse().model(),
    response_description=UserListResponse().get("description"),
)
def list_users():
    try:
        users = get_user_list()
        return UserListResponse().format(users)
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}
