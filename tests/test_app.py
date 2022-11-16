from fastapi.testclient import TestClient
from fastapi import status
from notifications_service.app import app
from notifications_service.model.notificationManager import NotificationManager

notificationManager = NotificationManager()
#client = TestClient(app)

def test_receiving_send_notification_requests_it_is_sent_correctly():
    device_token = "ExponentPushToken[UDA8pABqgFsu3ik3K9Sh8x]"
    notificationManager.send_push_message(device_token, "Prueba de notificacion ahora")
    assert True