"""Error definitions"""


# pylint: disable=too-few-public-methods
class Errors:
    """Class to store generic errors"""

    class NotFoundError(Exception):
        """Error raised when data is not found in database"""

        def __init__(self, message: str, system_code: int):
            super().__init__(self)
            self.message = message
            self.system_code = system_code

    class InvalidRequestError(Exception):
        """Error raised when request is invalid, due to input type being wrong
        or in incorrect format
        """

        def __init__(self, message: str, system_code: int):
            super().__init__(self)
            self.message = message
            self.system_code = system_code

    class UnauthAccessError(Exception):
        """Error raise when user is trying to consult unauthorized information"""

        def __init__(self, message: str, system_code: int):
            super().__init__(self)
            self.message = message
            self.system_code = system_code

    class ValidationError(Exception):
        """Error validating request"""

        def __init__(self, message: str, system_code: int):
            super().__init__(self)
            self.message = message
            self.system_code = system_code
