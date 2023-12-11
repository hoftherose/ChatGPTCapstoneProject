from fastapi import APIRouter

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import QuestionCreatedResponse, QuestionListResponse, QuestionResponse
from src.services.questions import *
from src.utils.constants import logging


questions_router = APIRouter(
    prefix="/api/v1/queries",
    tags=["Queries"],
    responses=ErrorResponses.all(),
)

@questions_router.get(
    "/list/{thread_id}",
    response_model=QuestionListResponse().model(),
    response_description=QuestionListResponse().get("description"),
)
def list_question(thread_id: str):
    questions = list_questions(thread_id)
    return QuestionListResponse().format(questions)

@questions_router.get(
    "/{question_id}",
    response_model=QuestionResponse().model(),
    response_description=QuestionResponse().get("description"),
)
def get_question(question_id: int):
    questions = get_questions(question_id)
    return QuestionResponse().format(questions)

@questions_router.post(
    "/generate/{assistant_id}",
    response_model=QuestionCreatedResponse().model(),
    response_description=QuestionCreatedResponse().get("description"),
)
def generate(assistant_id: str, num_questions: int = 10):
    questions = generate_questions(assistant_id, num_questions)
    return QuestionCreatedResponse().format(questions)
