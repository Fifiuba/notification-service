class UserInfoException(Exception):
    ...

class UserNotFoundError(UserInfoException):
    def __init__(self):
        self.status_code = 404 
        self.detail = "The user does not exists"

class NotificationException(Exception):
    def __init__(self):
        self.status_code = 409
        self.detail = "Notification failed"