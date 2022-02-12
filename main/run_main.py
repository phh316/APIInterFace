#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/12
# @Author : Ph
# @File : run_main.py

import unittest
from common.setting import MOUDLE_DIR_PATH, SUIT_PROJRCT
from common.HTMLTestRunner import HTMLTestRunner

#创建测试套件实例
suite = unittest.TestSuite()

#测试加载器的初始化
loader = unittest.defaultTestLoader

#加载测试对象
for test in SUIT_PROJRCT:
    test_suit = loader.discover(start_dir = MOUDLE_DIR_PATH,pattern = test)
    suite.addTest(test_suit)

with open('../report.html', 'wb') as f:
    runner = HTMLTestRunner(f, verbosity=2)
    runner.run(suite)
