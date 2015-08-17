"""This script contains all custom exceptions for the TBA API Module

"""

class APIUnavailableError(Exception):
    """Model for Error when can't connect to API

    Attributes:
        Message: String containing message to pass for exception.
    """
    def __init__(self, arg=None):
        default_message = 'API is not available. Check your connection.'
        if arg is not None:
            message = arg
        else:
            message = default_message
        Exception.__init__(self, message)
        self.message = message

class APPIDNotSetError(Exception):
    """Model for APPID not set Error

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, arg=None):
        default_message = 'API_APPID is not set. needs to be formatted as ' \
        '<team/person id>:<app description>:<version>.'
        if arg is not None:
            message = arg
        else:
            message = default_message
        Exception.__init__(self, message)
        self.message = message

class EventFormattingError(Exception):
    """Model for Event Formatting Error

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, arg=None):
        default_message = 'Event data is not properly formatted.'
        if arg is not None:
            message = arg
        else:
            message = default_message
        Exception.__init__(self, message)
        self.message = message

class MatchFormattingError(Exception):
    """Model for Match Formatting Error

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, arg=None):
        default_message = 'Match data is not properly formatted.'
        if arg is not None:
            message = arg
        else:
            message = default_message
        Exception.__init__(self, message)
        self.message = message

class ResourceUnavailableError(Exception):
    """Model for 404 Error

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, url=None, arg=None):
        default_message = 'Resource Unavailable. Please Check the URL'
        if arg is not None:
            message = arg
        elif url is not None:
            message = "%s: %s" % (default_message, url)
        else:
            message = "%s." % default_message
        Exception.__init__(self, message)
        self.message = message

class StatsFormattingError(Exception):
    """Model for Stats Formatting Error

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, arg=None):
        default_message = 'Stats data is not properly formatted.'
        if arg is not None:
            message = arg
        else:
            message = default_message
        Exception.__init__(self, message)
        self.message = message

class TeamFormattingError(Exception):
    """Model for Team Formatting Error

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, arg=None):
        default_message = 'Team data is not properly formatted.'
        if arg is not None:
            message = arg
        else:
            message = default_message
        Exception.__init__(self, message)
        self.message = message

class UnexpectedDataError(Exception):
    """Model for Unexpected Data being retreived from request.

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, url=None, arg=None):
        default_message = 'Unexpected data retrieved. Please Check the URL'
        if arg is not None:
            message = arg
        elif url is not None:
            message = "%s: %s" % (default_message, url)
        else:
            message = "%s." % default_message
        Exception.__init__(self, message)
        self.message = message

class YearsParticipatedFormattingError(Exception):
    """Model for YearsParticipated Formatting Error

    Attributes:
        message: String containing message to pass for exception.
    """
    def __init__(self, arg=None):
        default_message = 'Years Participated data is not properly formatted.'
        if arg is not None:
            message = arg
        else:
            message = default_message
        Exception.__init__(self, message)
        self.message = message
