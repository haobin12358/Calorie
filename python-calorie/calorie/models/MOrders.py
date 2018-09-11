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

class OrdersMain(BaseModel):
    __tablename__ = "OrdersMain"
    OMid = Column(String(64), primary_key=True)
    OMcreatetime = Column(DATETIME)                                 # 订单时间
    USid = Column(String(64), nullable=False)
    CPid = Column(String(64))                                       # 优惠券id
    OMprice = Column(Float)                                         # 订单总价
    OMway = Column(Integer, nullable=False, default=500)            # 取货方式，500自提501同城502快递
    LOid = Column(String(64))                                       # 取货地址，501&502用
    OMtelphone = Column(String(32))                                 # 联系方式，500用
    OMtime = Column(Integer, default=600)                           # 取餐时间，600随机时段601时段1递推，500&501用
    OMstatus = Column(Integer, default=700)                         # 订单状态，700未支付701已支付702配送中703已签收704已评价705退款中706已退款
    OMmessage = Column(String(2000))                                # 订单留言

class OrdersPart(BaseModel):
    __tablename__ = "OrdersPart"
    OPid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)
    PRnumber = Column(Integer, nullable=False, default=1)           # 商品数量
    OMid = Column(String(64), nullable=False)

class OrdersCart(BaseModel):
    __tablename__ = "OrdersCart"
    OCid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)                       # 用户
    LAid = Column(String(64), nullable=False)                       # 区域
    OCstatus = Column(Integer, default=1)                           # 购物车商品状态，0不可用1可用
    PRid = Column(String(64), nullable=False)                       # 商品
    PRnumber = Column(Integer, default=1)                           # 商品数目
    OCcreatetime = Column(DATETIME)                                 # 创建时间
    OCupdatetime = Column(DATETIME)                                 # 更新时间

class OrdersReview(BaseModel):
    __tablename__ = "OrdersReview"
    ORid = Column(String(64), primary_key=True)
    OMid = Column(String(64), nullable=False)
    ORmessage = Column(String(2000))                                # 订单评价，基于订单
    ORscore = Column(Float)                                         # 订单总体评分