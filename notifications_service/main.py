import uvicorn
from notifications_service.app import app
from notifications_service.database import database
from notifications_service.utils.FCMManager import FCMManager

database.init_database()
global fmc
fmc = FCMManager()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)