from pydantic import BaseModel


class RoadRegisterInput(BaseModel):
    adres:str
    kilometer:str
    reference_point:str

class CamRegisterInput(BaseModel):
    token:str
    road_id:int
    traffic_light_distance:float
    road_speed:int

class TraficLightInput(BaseModel):
    token:str
    road_id:int
    closed:bool
    priority:int