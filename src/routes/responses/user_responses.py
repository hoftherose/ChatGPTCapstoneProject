"""Response model for next payment amount"""
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

from src.utils import SystemCodes
from src.routes.responses.base import BaseResponse


class UserSchema(BaseModel):
    """Schema for Users"""

    id: str
    name: str

class UserResponse(BaseResponse):
    """Response for users"""

    message: str = "User successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        user: UserSchema

class UserListResponse(BaseResponse):
    """Response for user lists"""

    message: str = "user list successfully obtained"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        users: List[UserSchema]
