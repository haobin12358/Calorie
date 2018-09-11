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

class Users(BaseModel):
    __tablename__ = "Users"
    USid = Column(String(64), primary_key=True)
    USname = Column(String(200))                        # 昵称，默认用微信昵称
    USsex = Column(Integer)                             # 性别
    UScoin = Column(Float, default=0)                   # 积分
    USprovince = Column(String(200))                    # 省份，微信记录
    UScity = Column(String(200))                        # 城市，微信记录
    USopenid = Column(String(200))                      # 微信关联id
    USwechatname = Column(String(200))                  # 微信昵称
    UStelphone = Column(String(32))                     # 手机号，默认绑定微信手机号，可更换
    UScreatetime = Column(DATETIME)                     # 创建时间，记录注册用户
    USupdatetime = Column(DATETIME)                     # 更新时间，记录用户数据更新
    USstatus = Column(Integer, default=100)             # 用户状态，100未认证101认证中102认证通过103认证不通过104黑名单

class UsersFirst(BaseModel):
    __tablename__ = "UsersFirst"
    UFid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)
    USheight = Column(Float)                            # 身高
    USweight = Column(Float)                            # 体重
    USbirthday = Column(DATE)                           # 生日

class UsersSecond(BaseModel):
    __tablename__ = "UsersSecond"
    USSid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)
    UScompany = Column(String(2000))                    # 公司信息
    USworker = Column(String(2000))                     # 职业

class UsersLike(BaseModel):
    __tablename__ = "UsersLike"
    ULid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)
    ULsweet = Column(Integer, default=0)                # 甜,0表示不喜欢，1表示喜欢，下同
    ULhot = Column(Integer, default=0)                  # 辣
    ULsalty = Column(Integer, default=0)                # 咸
    ULacid = Column(Integer, default=0)                 # 酸
    ULbitter = Column(Integer, default=0)               # 苦

class UsersCertification(BaseModel):
    __tablename__ = "UsersCertification"
    UCid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)
    UCcardno = Column(String(64), nullable=False)       # 身份证号
    UCcardpositive = Column(String(200))                # 身份证正面
    UCcardnegative = Column(String(200))                # 身份证反面
    UCuserface = Column(String(200))                    # 人脸图像
    UCtruename = Column(String(200))                    # 真实姓名

class Locations(BaseModel):
    __tablename__ = "Locations"
    LOid = Column(String(64), primary_key=True)
    USid = Column(String(64), nullable=False)
    LOname = Column(String(200))                        # 收件人姓名
    LOtelphone = Column(String(200))                    # 收件人联系方式
    LAid = Column(String(200))
    LOmessage = Column(String(2000))                    # 收件人详细地址
    LOlabel = Column(Integer, default=200)              # 标签，201默认202已关闭200其他