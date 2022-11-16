class UserInfoException(Exception):
    ...

class UserNotFoundError(UserInfoException):
    def __init__(self):
        self.status_code = 404 
        self.detail = "The user does not exists"