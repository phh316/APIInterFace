#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/14
# @Author : Ph
# @File : __init__.py
from common.get_data import Config
from common.get_excel import GetData
from common.log import Log
from common.get_data import ExcelData

log = Log.get_log()
excel = ExcelData()


def count(i):
    print(Config().get_value('sheet', 'run_module1'))
    print(i)
    data = GetData(Config().get_value('sheet', 'run_module1'))
    # count = data.get_lines()