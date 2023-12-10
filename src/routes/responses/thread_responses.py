"""Response model for next payment amount"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from src.utils import SystemCodes
from src.routes.responses.base import BaseResponse


class ThreadSchema(BaseModel):
    """Schema for threads"""

    id: str
    name: str

class ThreadResponse(BaseResponse):
    """Response for threads"""

    message: str = "Thread successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        thread: ThreadSchema

class ThreadListResponse(BaseResponse):
    """Response for thread lists"""

    message: str = "Thread list successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        threads: List[ThreadSchema]
