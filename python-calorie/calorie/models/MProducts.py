# -*- coding:utf8 -*-
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import Column, create_engine, Integer, String, Text, Float, Boolean, orm, DATETIME, DATE
from calorie.config import dbconfig as cfg
from calorie.models.base_model import BaseModel, auto_createtime

DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename,
    cfg.username,
    cfg.password,
    cfg.host,
    cfg.database,
    cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False)

class Products(BaseModel):
    __tablename__ = "Products"
    PRid = Column(String(64), primary_key=True)
    PRname = Column(String(200), nullable=False)            # 商品名称
    PRimage = Column(String(200))                           # 商品图片
    PRinfo = Column(String(1000))                           # 商品详情
    PRprice = Column(Float)                                 # 商品价格
    PRdprice = Column(Float)                                # 商品折扣价
    PRvolume = Column(Integer)                              # 商品销量
    PRscore = Column(Float)                                 # 商品评分
    PRstatus = Column(Integer, default=300)                 # 商品状态，300待审301在售302已下架
    BRid = Column(String(64), primary_key=True)             # 只记录末端叶子节点类目id，利用叶子节点寻找父类目
    LAid = Column(String(64), nullable=False)               # 用于判断属于哪个区域的商品，如果为空则代表区域不限制

class Brands(BaseModel):
    __tablename__ = "Brands"
    BRid = Column(String(64),primary_key=True)
    BRname = Column(String(2000))                                       # 商品类目名称
    BRfromid = Column(String(64), nullable=False, default="0")          # 商品父类目id

class ProductsType(BaseModel):
    __tablename__ = "ProductsType"
    PTid = Column(String(64), primary_key=True)
    PTname = Column(String(200))                            # 商品属性名称
    PTvalue = Column(String(1000))                          # 商品属性值
    PRid = Column(String(64), nullable=False)

class ProductsIcon(BaseModel):
    __tablename__ = "ProductsIcon"
    PIid = Column(String(64), primary_key=True)
    PIname = Column(String(200), nullable=False)            # 标签名称
    PRid = Column(String(64), nullable=False)
    PIstatus = Column(Integer, default=400)                 # 标签状态400使用中401已废弃

class ProductsReview(BaseModel):
    __tablename__ = "ProductsReview"
    PWid = Column(String(64), primary_key=True)
    PWmessage = Column(String(2000))                        # 评论内容，基于商品
    PRscore = Column(Float)                                 # 评论分数，基于商品

