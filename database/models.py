from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Road(Base):
    __tablename__='road'
    id = Column(Integer, primary_key=True, autoincrement=True)
    adres = Column(String)
    kilometer = Column(String)
    reference_point = Column(String)
    # traffic_light = relationship('Traffic_Light', backref='road')
    # Cam = relationship('Cam', backref='road')


class Cam(Base):
    __tablename__='cam'
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String (10))
    road_id = Column(Integer, ForeignKey('road.id'))
    traffic_light_distance = Column(Float)
    road_speed = Column(Integer)
    # traffic_light = relationship('Traffic_Light', backref='cam')

class Traffic_Light(Base):
    __tablename__='traffic_light'
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String (10))
    road_id = Column(Integer, ForeignKey('road.id'))
    cam_id = Column(Integer, ForeignKey('cam.id'))
    closed = Column(Boolean)
    priority = Column(Integer)


class Service_Cam(Base):
    __tablename__='service_cam'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cam_id = Column(Integer, ForeignKey('cam.id'))
    vehicle_count = (Integer)
    


class Order_Service_Cam(Base):
    __tablename__='orders_service_cam'
    id = Column(Integer, primary_key=True, autoincrement=True)
    reset = Column(Boolean)
    cam_id = Column(Integer, ForeignKey('cam.id'))
    


class Order_Service_Traffic_Light(Base):
    __tablename__='orders_service_traffic_light'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time_to_open = (Float)
    traffic_light_id = Column(Integer, ForeignKey('traffic_light.id'))
    