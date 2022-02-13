#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/1/12
# @Author : Ph
# @File : module_1.py
import unittest
from unittest import skip, skipIf, skipUnless
from os import name
from sys import version_info, platform
# @skip  跳过
# @skipif 条件为 true 跳过
# @skipUnless 条件为false 跳过

from run.run_test import RunTest
from common.get_config import Config
from common.get_data import GetData
from common.log import Log
from common.get_excel import ExcelData
from functools import wraps


class TestCase(unittest.TestCase):

    def _init(func):
        @wraps(func)
        def inner_func(self):
            self.data = GetData(Config().get_value('sheet', 'isRun'))
            self.count = self.data.get_lines()
            self.log = Log.get_log()
            self.excel = ExcelData()
            func(self)
        return inner_func

    @_init
    def test_module1(self):
        for i in range(1, self.count):
            except_result = self.data.get_except_result(i)
            res = RunTest().runner(i)
            if except_result in res:
                self.excel.wirte_value(i, "pass")
                self.log.info(f"断言匹配条件为 :{except_result} 匹配结果为 : True，案例执行pass")
            else:
                self.log.error(f"断言匹配条件为 :{except_result} 匹配结果为 : True，案例执行failed")
                self.excel.wirte_value(i, res)
