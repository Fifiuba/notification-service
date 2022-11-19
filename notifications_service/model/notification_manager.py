from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError
from notifications_service.database.exceptions import NotificationException

class NotificationManager:

    def send_push_message(self, token,title, body, data=None):
        try:
            message = PushMessage(to=token,title=title,body=body,data=data,priority='high',display_in_foreground=False)
            response = PushClient().publish(message)
            self.validate_response(response)
            return response.status
        except PushServerError as exc:
            print(str(exc))
            raise NotificationException
        except (ConnectionError, HTTPError) as exc:
            print(str(exc))
            raise NotificationException

        
    
    def validate_response(self,response):
        try:
            response.validate_response()
        except Exception as exc:
            print(str(exc))
            raise NotificationException