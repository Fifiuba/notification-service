from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from notifications_service.controllers import notification_controller

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def welcome():
    return "Notification Service!"

app.include_router(notification_controller.notification_router, prefix="/notification", tags=["Notification"])