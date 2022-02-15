#!/usr/bin/env python
# -- coding: utf-8 --
# @Author : Ph
# @File : run_main.py
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from common.setting import MOUDLE_DIR_PATH, SUIT_PROJRCT,REPORT_DIR_PATH,REPORT_FILE_PATH
from common.HTMLTestRunner import HTMLTestRunner

file_path = REPORT_DIR_PATH+REPORT_FILE_PATH

# #创建测试套件实例
suite = unittest.TestSuite()

# #测试加载器的初始化
loader = unittest.defaultTestLoader

#加载测试对象
for test in SUIT_PROJRCT:
    test_suit = loader.discover(start_dir = MOUDLE_DIR_PATH,pattern = test)
    suite.addTest(test_suit)


if os.path.exists(file_path):
    os.remove(file_path)
with open('../report/report.html', 'wb') as f:
    runner = HTMLTestRunner(f, title='自动化测试报告', verbosity=2)
    runner.run(suite)
