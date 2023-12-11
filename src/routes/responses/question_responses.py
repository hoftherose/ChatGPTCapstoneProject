"""Response model for next payment amount"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from src.utils import SystemCodes
from src.routes.responses.base import BaseResponse


class QuestionSchema(BaseModel):
    """Schema for questions"""

    message: str

class QuestionCreatedResponse(BaseResponse):
    """Response for questoins"""

    message: str = "Questions successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        questions: List[QuestionSchema]

class QuestionResponse(BaseResponse):
    """Response for questions"""

    message: str = "Question successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        questions: QuestionSchema
