#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2021/7/12
# @Author : Ph
# @File : module_1.py
import unittest

from module import out_func
from run.run_test import RunTest


class TestCaseM2(unittest.TestCase):

    @out_func(i = 1)
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
