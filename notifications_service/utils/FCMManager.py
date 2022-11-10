import firebase_admin
from firebase_admin import credentials


#TODO: chequear si no puedo usar una bd de firebase. 
#firebase_admin.initialize_app(cred, {'databaseURL': 'url'})

class FCMManager:
    def __init__(self):
        self.cred = credentials.Certificate("notifications_service/utils/firebase_keys.json")
        self.default_app = firebase_admin.initialize_app(self.cred)


    def sendPush(self, deviceTokens, data=None, title=None, body=None):
        #TODO: cheqeuar si esta bien que sea multicast (decia que era para mandarle a varios tokens a la vez)

        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title, 
                body=body
            ),
            tokens=deviceTokens,
            data=data
        )

        return messaging.send_multicast(message)