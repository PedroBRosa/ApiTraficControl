

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
    ServicesLight
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

@road_router.delete('/delete/{road_id}', response_model=StandardOutPut, responses={400: {'model': ErrorOutput}})
async def road_delete(road_id: int):
    try:
       await ServicesRoad.delete_road(road_id)
       return StandardOutPut(message='Via deletada com sucesso') 
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


@cam_router.delete('/delete/{cam_id}', response_model=StandardOutPut, responses={400: {'model': ErrorOutput}})
async def cam_delete(cam_id: int):
    try:
       await ServicesCam.delete_cam(cam_id)
       return StandardOutPut(message='Camera deletada com sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@traffic_light_router.post('/register',description='My description', response_model=StandardOutPut, responses={400: {'model': ErrorOutput}})
async def traffic_light_register(traffic_light_imput: TraficLightInput):
    try:
       await ServicesLight.register_trafic_light(
            token = traffic_light_imput.token,
            road_id = traffic_light_imput.road_id,
            closed = traffic_light_imput.closed,
            priority = traffic_light_imput.priority
       )
       return StandardOutPut(message='Sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@traffic_light_router.delete('/delete/{trafic_light_id}', response_model=StandardOutPut, responses={400: {'model': ErrorOutput}})
async def trafic_light_id_delete(trafic_light_id: int):
    try:
       await ServicesLight.delete_trafic_light(trafic_light_id)
       return StandardOutPut(message='Sinal deletado com sucesso') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    #