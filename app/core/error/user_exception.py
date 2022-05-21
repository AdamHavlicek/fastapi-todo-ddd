"""
    User exceptions
"""


class UserNotFoundError(Exception):
    message = 'User does not exist.'

    def __str__(self):
        return UserNotFoundError.message


class UsersNotFoundError(Exception):
    message = 'Users do not exist'

    def __str__(self):
        return UsersNotFoundError.message


class UserAlreadyExistsError(Exception):
    message = 'User already exists'

    def __str__(self):
        return UserAlreadyExistsError.message
