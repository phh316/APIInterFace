#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/15
# @Author : Ph
# @File : __init__.py

from common.get_config import Config
from common.get_json import JsonData
from common.get_excel import ExcelData
from common.get_data import GetData
from common.log import Log
from common.setting import DATA_DIR_PATH,BASE_INI_PATH
import os


depend_id = int(Config().get_value('excel', 'dependentId'))
depend_data = int(Config().get_value('excel', 'dependentData'))
depend_para = int(Config().get_value('excel', 'dependentPara'))
file_name = os.path.join(DATA_DIR_PATH, "CaseEntity.xlsx")
is_default = Config().get_value('sheet', 'default')
config_name = BASE_INI_PATH

"""excel列数"""
header_col = int(Config().get_value('excel', 'header'))
method_col = int(Config().get_value('excel', 'method'))
url_col = int(Config().get_value('excel', 'url'))
name_col = int(Config().get_value('excel', 'name'))
case_col = int(Config().get_value('excel', 'case'))
exceptResult_col = int(Config().get_value('excel', 'exceptResult'))
isRun_col = int(Config().get_value('excel', 'isRun'))
