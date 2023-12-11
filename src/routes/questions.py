from fastapi import APIRouter

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import QuestionCreatedResponse
from src.services.questions import *
from src.utils.constants import logging


questions_router = APIRouter(
    prefix="/api/v1/queries",
    tags=["Queries"],
    responses=ErrorResponses.all(),
)

@questions_router.post(
    "/generate/{assistant_id}",
    response_model=QuestionCreatedResponse().model(),
    response_description=QuestionCreatedResponse().get("description"),
)
def generate(assistant_id: str, num_questions: int = 10):
    questions = generate_questions(assistant_id, num_questions)
    return QuestionCreatedResponse().format(questions)
