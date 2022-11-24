

from fastapi import APIRouter, HTTPException
from starlette import responses

from schemas import (
    RoadRegisterInput,
    CamRegisterInput,
    TraficLightInput,
    StandardOutPut,
    ErrorOutput
)
from services import (
    ServicesRoad,
    ServicesCam,
    ServicesTraficLight
)

road_router = APIRouter(prefix='/road')
cam_router = APIRouter(prefix='/cam')
traffic_light_router = APIRouter(prefix='/traffic_light')

@road_router.post('/register', description='My description', response_model=StandardOutPut, responses={400: {'model': ErrorOutput}})
async def road_register(road_imput: RoadRegisterInput):
    try:
       await ServicesRoad.register_road(
        adres=road_imput.adres,
        kilometer=road_imput.kilometer,
        reference_point=road_imput.reference_point
       )
       return StandardOutPut(message='Sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))




@cam_router.post('/register',description='My description', response_model=StandardOutPut, responses={400: {'model': ErrorOutput}})
async def cam_register(cam_imput: CamRegisterInput):
    try:
       await ServicesCam.register_cam(
            token=cam_imput.token,
            road_id=cam_imput.road_id,
            traffic_light_distance=cam_imput.traffic_light_distance,
            road_speed=cam_imput.road_speed
       )
       return StandardOutPut(message='Sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))





@traffic_light_router.post('/register',description='My description', response_model=StandardOutPut, responses={400: {'model': ErrorOutput}})
async def traffic_light_register(traffic_light_imput: TraficLightInput):
    try:
       await ServicesTraficLight.register_traffic_light(
            token = traffic_light_imput.token,
            road_id = traffic_light_imput.road_id,
            closed = traffic_light_imput.closed,
            priority = traffic_light_imput.priority
       )
       return StandardOutPut(message='Sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

