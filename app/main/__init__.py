# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 16:54
# @Author  : shuyong

from  flask import Blueprint
# 定义蓝本
main = Blueprint('main', __name__)

from . import views, errors

