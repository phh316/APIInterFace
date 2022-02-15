#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/15
# @Author : Ph
# @File : __init__.py

from common.get_config import Config
from common.setting import DATA_DIR_PATH
import os

"""excel 初始化设置"""
depend_id = int(Config().get_value('excel', 'dependentId'))
depend_data = int(Config().get_value('excel', 'dependentData'))
depend_para = int(Config().get_value('excel', 'dependentPara'))
file_name = os.path.join(DATA_DIR_PATH, "CaseEntity.xlsx")
is_default = Config().get_value('sheet', 'default')
sheet_names = Config().get_value('sheet', 'run_module').split(',')
