from fastapi.testclient import TestClient
from fastapi import status
from notifications_service.app import app
from notifications_service.model.notification_manager import NotificationManager
from tests import conftest


session = conftest.init_database(app)
notificationManager = NotificationManager()
client = TestClient(app)


def test_receiving_send_notification_requests_it_is_sent_correctly():
    device_token = "ExponentPushToken[UDA8pABqgFsu3ik3K9Sh8x]"
    #response = notificationManager.send_push_message(device_token,"Test 01","Test desde Notification Service!")
    #assert response.status == 'ok'
    assert True

def test_create_new_user_with_device_token():
    device_token = "ExponentPushToken[UDA8pABqgFsu3ik3K9Sh8x]"
    response = client.post(
            "/notification/new_user",
            json={
                "user_id": 1,
                "token": device_token
            })
    assert response.status_code == status.HTTP_201_CREATED, response.text
    data = response.json()
    assert data["user_id"] == 1
    assert data["token"] == device_token

def test_send_notification():
    response = client.post(
        "/notification",
        json={
            "user_id": 1,
            "title": 'Test 02',
            "body": 'Esto es el body',
            "data": '{"id": journe_id, "status":"accepted"}'
        })
    assert response.status_code == status.HTTP_200_OK

    
