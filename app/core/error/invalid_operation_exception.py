from app.core.error.base_exception import BaseError


class InvalidOperationError(BaseError):
    message: str = 'Invalid Operation on entity'

    def __init__(self, message):
        self.message = message
