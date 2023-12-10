"""Response model for next payment amount"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from src.utils import SystemCodes
from src.routes.responses.base import BaseResponse


class ToolSchema(BaseModel):
    """Schema for tools"""
    type: str

class AssistantSchema(BaseModel):
    """Schema for assistants"""

    id: str
    created_at: datetime
    file_ids: List[str]
    instructions: str
    model: str
    name: str

class AssistantCreatedResponse(BaseResponse):
    """Response for assistants"""

    message: str = "Assistant successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        assistant: List[AssistantSchema]

class AssistantResponse(BaseResponse):
    """Response for assistants"""

    message: str = "Assistant successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        assistant: AssistantSchema

class AssistantListResponse(BaseResponse):
    """Response for assistant lists"""

    message: str = "Assistant list successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        num_assistants: int
        assistants: List[AssistantSchema]
