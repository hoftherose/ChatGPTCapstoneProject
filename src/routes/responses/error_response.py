"""Error response outlines"""
from src.routes.responses.base import BaseErrors, BaseResponse
from src.utils import StatusCodes, SystemCodes


class ErrorResponses(BaseErrors):
    """Class to store all generic error responses"""

    class NotFound(BaseResponse):
        """Item not found in database"""

        status_code: int = StatusCodes.NOT_FOUND
        description: str = "Not Found"
        message: str = "Object was not found"
        code: int = SystemCodes.TEST_NOT_FOUND

    class InvalidRequest(BaseResponse):
        """Request Invalid"""

        status_code: int = StatusCodes.BAD_REQUEST
        description: str = "Bad Request"
        message: str = "Incorrect request format"
        code: int = SystemCodes.TEST_BAD_REQUEST

    class UnauthAccess(BaseResponse):
        """Unauthorized access"""

        status_code: int = StatusCodes.UNAUTHORIZED
        description: str = "Unauthorized Access"
        message: str = "User does not have access to item"
        code: int = SystemCodes.TEST_UNAUTH_ACCESS

    class ValidationError(BaseResponse):
        """Validation error"""

        status_code: int = StatusCodes.VALIDATION_ERROR
        description: str = "Validation Error"
        message: str = "Error validating input type"
        code: int = SystemCodes.TEST_VALIDATION_ERROR

    class ServerError(BaseResponse):
        """Server error"""

        status_code: int = StatusCodes.SERVER_ERROR
        description: str = "Server Error"
        message: str = "Internal server error type"
        code: int = SystemCodes.TEST_SERVER_ERROR
