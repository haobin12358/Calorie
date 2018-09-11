# -*- coding:utf8 -*-
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import Column, create_engine, String
from calorie.config import dbconfig as cfg
from calorie.models.base_model import BaseModel

DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename,
    cfg.username,
    cfg.password,
    cfg.host,
    cfg.database,
    cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False)

class LocationsProvince(BaseModel):
    __tablename__ = "LocationProvince"
    LPid = Column(String(64), primary_key=True)
    LPname = Column(String(1000), nullable=False)       # 省份名称

class LocationsCity(BaseModel):
    __tablename__ = "LocationCity"
    LCid = Column(String(64), primary_key=True)
    LPid = Column(String(64), nullable=False)
    LCname = Column(String(1000), nullable=False)       # 城市名称

class LocationsTownship(BaseModel):
    __tablename__ = "LocationsTownship"
    LTid = Column(String(64), primary_key=True)
    LCid = Column(String(64), nullable=False)
    LTname = Column(String(1000), nullable=False)       # 城区名称

class LocationsArea(BaseModel):
    __tablename__ = "LocationsArea"
    LAid = Column(String(64), primary_key=True)
    LTid = Column(String(64), nullable=False)
    LAname = Column(String(1000), nullable=False)       # 自定义区域名称