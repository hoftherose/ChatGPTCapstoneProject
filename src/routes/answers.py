from fastapi import APIRouter

from src.routes.responses.error_response import ErrorResponses
from src.routes.responses import *
from src.services.answers import review_answer


answers_router = APIRouter(
    prefix="/api/v1/answers",
    tags=["Answers"],
    responses=ErrorResponses.all(),
)

@answers_router.post(
    "/{question_id}",
    response_model=AnswerResponse().model(),
    response_description=AnswerResponse().get("description"),
)

def answer_question(question_id: int, answer: str):
    result = review_answer(question_id, answer)
    return AnswerResponse().format(result)
