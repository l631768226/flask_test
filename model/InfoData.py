# -- coding: utf-8 --
from datetime import datetime
from decimal import Decimal

from pymysql import Timestamp

from app import db
from dataclasses import dataclass


def query_set_to_dict(obj, conv=False):
    obj_dict = {}
    for column in obj.__table__.columns.keys():
        val = getattr(obj, column)
        if isinstance(val, Decimal):
            val = float(val)
        if isinstance(val, datetime):
            if conv:
                val = Timestamp(seconds=int(val.timestamp()))
            else:
                val = val.strftime("%Y-%m-%d %H:%M:%S")
        obj_dict[column] = val
    return obj_dict


def query_set_to_list(querySet, conv=False):
    ret_list = []
    for obj in querySet:
        ret_dict = query_set_to_dict(obj, conv)
        ret_list.append(ret_dict)
    return ret_list


@dataclass
class NewsInfo(db.Model):
    __tablename__ = 'news_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.TEXT, nullable=True)
    time_str = db.Column(db.String(11), nullable=True)
    info = db.Column(db.String(100), nullable=True)
    sort = db.Column(db.Integer, nullable=True)
    img_path = db.Column(db.String(255), nullable=True)


@dataclass
class ProInfo(db.Model):
    __tablename__ = 'pro_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pro_name = db.Column(db.String(100), nullable=True)
    dept_name = db.Column(db.String(100), nullable=True)
    pro_labels = db.Column(db.String, nullable=True)
    pro_prin = db.Column(db.String, nullable=True)
    contant = db.Column(db.String)
    pro_des = db.Column(db.String)
    pro_func = db.Column(db.String)
    pro_case = db.Column(db.String)
    pro_info = db.Column(db.String)
    pro_vedio = db.Column(db.String)
    pro_class = db.Column(db.String)
    pro_img = db.Column(db.String)
    sort = db.Column(db.Integer)


@dataclass
class ProImg(db.Model):
    __tablename__ = 'pro_img'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pro_id = db.Column(db.Integer)
    img_path = db.Column(db.String)
    sort = db.Column(db.Integer)
    del_flag = db.Column(db.String)