
from database.models import *
from database.connection import engine
from sqlalchemy.ext.asyncio.session import  AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete


class ServicesRoad:
    async def register_road(adres,kilometer,reference_point):
        async with AsyncSession(engine) as session:
            session.add(Road(
            adres=adres,
            kilometer=kilometer,
            reference_point=reference_point,
            ))
            await session.commit()

    async def delete_road(road_id):
        async with AsyncSession(engine) as session:
            await session.execute(delete(Road).where(Road.id==road_id))
            await session.commit()

class ServicesCam:
    async def register_cam(token,road_id,traffic_light_distance,road_speed):
        async with AsyncSession(engine) as session:
            session.add(Cam(
                token=token,
                road_id=road_id,
                traffic_light_distance=traffic_light_distance,
                road_speed=road_speed
            ))
            await session.commit()

    async def delete_cam(cam_id):
        async with AsyncSession(engine) as session:
            await session.execute(delete(Cam).where(Cam.id==cam_id))
            await session.commit()

class ServicesLight:
    async def register_trafic_light(token,road_id,closed,priority):
        async with AsyncSession(engine) as session:
            session.add(Traffic_Light(
                token=token,
                road_id=road_id,
                closed=closed,
                priority=priority
            ))
            await session.commit()

    async def delete_trafic_light(trafic_light_id):
        async with AsyncSession(engine) as session:
            await session.execute(delete(Traffic_Light).where(Traffic_Light.id==trafic_light_id))
            await session.commit()