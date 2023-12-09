"""System code definitions"""


# pylint: disable=too-few-public-methods
class SystemCodes:
    """Micro-service system codes, used for reviewing documentation
    Default value is UNDEFINED, which will return 0.
    There are more values that extend UNDEFINED for readibilty only.
    """

    UNDEFINED = 0

    UNKNOWN_ISSUE = 1000
    SUCCESSFUL_QUERY = 1001
