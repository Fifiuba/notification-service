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
    data = {'service': 'Notification service!',
    'created_on':'2-11-2022',
    'description':'Notificacion service is the responsable of sending push notifications to correct users, it uses Expo servers to do this job.'}
    return data

app.include_router(notification_controller.notification_router, prefix="/notification", tags=["Notification"])