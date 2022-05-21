

class BaseError(Exception):

    message: str = 'Server Internal Error'

    def __str__(self):
        return self.message

    # def __init__(self, message):
    #     self.message = message
