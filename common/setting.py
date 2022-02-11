#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/10
# @Author : Ph
# @File : setting.py
import os

'''设置文件基础路径'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMON_DIR_PATH = os.path.join(BASE_DIR,'common')
CONFIG_DIR_PATH = os.path.join(BASE_DIR,'config')
BASE_INI_PATH = os.path.join(CONFIG_DIR_PATH,'base.ini')
DATA_DIR_PATH = os.path.join(BASE_DIR,'case')
LOG_DIR_PATH = os.path.join(BASE_DIR,'log')
LIB_DIR_PATH = os.path.join(BASE_DIR,'lib')
REPORT_DIR_PATH = os.path.join(BASE_DIR,'report')
CASE_DIR_PATH = os.path.join(BASE_DIR,'case')



'''报文头设置'''
HEADER = {"key": "Content-Type", "value": "application/json", "description": ""}



