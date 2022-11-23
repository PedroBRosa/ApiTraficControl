from fastapi import APIRouter
from schemas import *
from services import *

road_router = APIRouter(prefix='/road')
cam_router = APIRouter(prefix='/cam')
traffic_light_router = APIRouter(prefix='/traffic_light')

@road_router.post('/register')
async def road_register(road_imput: RoadRegisterInput):
    try:
       await ServicesRoad.register_road(
        adres=road_imput.adres,
        kilometer=road_imput.kilometer,
        reference_point=road_imput.reference_point
       )
    except:
        pass

@cam_router.post('/register')
async def cam_register(cam_imput: CamRegisterInput):
    try:
       await ServicesCam.register_cam(
            token=cam_imput.token,
            road_id=cam_imput.road_id,
            traffic_light_distance=cam_imput.traffic_light_distance,
            road_speed=cam_imput.road_speed
       )
    except:
        pass

@traffic_light_router.post('/register')
async def traffic_light_register(traffic_light_imput: TraficLightInput):
    try:
       await ServicesTraficLight.register_traffic_light(
            token = traffic_light_imput.token,
            road_id = traffic_light_imput.road_id,
            closed = traffic_light_imput.closed,
            priority = traffic_light_imput.priority
       )
    except:
        pass