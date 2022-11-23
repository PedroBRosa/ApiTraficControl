from fastapi import FastAPI, APIRouter
from views import *


app = FastAPI()
router = APIRouter()
cam = APIRouter()
traffic_light = APIRouter()

@router.get('/')
def frist():
    return 'Hello World!'

app.include_router(prefix='/index', router=router)
app.include_router(road_router)
app.include_router(cam_router)
app.include_router(traffic_light_router)
