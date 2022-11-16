from exponent_server_sdk import (
    PushClient,
    PushMessage,
)
from requests.exceptions import ConnectionError, HTTPError

class NotificationManager:

    def send_push_message(self, token,title, body, data=None):
        try:
            response = PushClient().publish(
                PushMessage(to=token,
                            title=title,
                            body=body,
                            data=data,
                            display_in_foreground=False))
            return response
        except Exception as exc:
            print(str(exc))