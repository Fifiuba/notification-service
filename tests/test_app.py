from fastapi.testclient import TestClient
from fastapi import status
from notifications_service.app import app
from notifications_service.model.notification_manager import NotificationManager

notificationManager = NotificationManager()
#client = TestClient(app)

def test_receiving_send_notification_requests_it_is_sent_correctly():
    device_token = "ExponentPushToken[UDA8pABqgFsu3ik3K9Sh8x]"
    response = notificationManager.send_push_message(device_token,"Test 01","Test desde Notification Service!")
    assert response.status == 'ok'

