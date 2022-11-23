from database.models import *
from database.connection import async_session


class ServicesRoad:
    async def register_road(adres,kilometer,reference_point):
        async with async_session() as session:
            session.add(Road(
            adres=adres,
            kilometer=kilometer,
            reference_point=reference_point,
            ))
            await session.commit()


class ServicesCam:
    async def register_cam(token,road_id,traffic_light_distance,road_speed):
        async with async_session() as session:
            session.add(Cam(
                token=token,
                road_id=road_id,
                traffic_light_distance=traffic_light_distance,
                road_speed=road_speed
            ))
            await session.commit()

class ServicesTraficLight:
    async def register_cam(token,road_id,closed,priority):
        async with async_session() as session:
            session.add(Cam(
                token=token,
                road_id=road_id,
                closed=closed,
                priority=priority
            ))
            await session.commit()
