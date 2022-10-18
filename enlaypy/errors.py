class EnlayException(Exception):
    """Base class for other exceptions"""
    pass

class NotAuthorized(EnlayException):
    """Raised when user is not authorized"""

    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)

class NotFound(EnlayException):
    """Raised when something is not found"""

    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)

class OtherError(EnlayException):
    """Raised when there is an error but it has an unknown code"""

    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)
