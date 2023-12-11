"""Response model for next payment amount"""
from pydantic import BaseModel

from src.utils import SystemCodes
from src.routes.responses.base import BaseResponse


class AnswerResponse(BaseResponse):
    """Response for questoins"""

    message: str = "Questions successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        result: str
        observation: str
