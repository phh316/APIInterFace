# -*- coding: utf-8 -*-
#
# def f(x):
#     return {
#         "plan-0": 1,
#         1: "plan-1",
#         2: "plan-2"
#     }.get(x, "plan-default")
#
# print(f('plan-0'))
# import requests
#
# r = requests.post("https://www.fastmock.site/mock/db8122608751bfc0a73df8b9e3da74ad/test/api/test")
# print(r.status_code)

# import re
# import sys
# sys.path.append("/opt/interface/APIInterface")
# print(sys.path)

#
# """
# """

# a = 'C|C464++|Jav4646a|C#|Pytho4545n|JavaScript'
# print(re.findall('\d',a))
# print(re.findall('\D',a))
# """
# \w  [A-Za-z0-9_]
# \W 非[A-Za-z0-9_] 包含空格、制表符
# \d
# \D
# \s 空白字符 空格、制表符等
# \S 非空白字符
#
# 数量词
#
# """
# b = 'abc, acc, adc, aec, afc, ahc'
# b = 'pytho 1323212jaPython1va612Pythonnn2scale'
# r = re.findall('Python{1,2}?',b)
# print(r)

# a = '2333333'
# a1 = '12345678'
# a2 = '10000001'
# r = re.findall('\d{4,8}',a)
# r1 = re.findall('^\d{4,8}$',a1)
# r2 = re.findall('^000',a2)
# r3 = re.findall('000$',a2)
# r4 = re.findall('^000$',a2)
# print(str(r)+"  "+str(r1)+"   "+str(r2)+"    "+str(r3)+"  "+str(r4))

# c = 'PythonPythonPythonPythonPythonPython'
# print(re.findall('(Python){4}',c))

# d = 'Pythonc#\nJavaPHP'
# print(re.findall('c#.{1}',d,re.I|re.S))


# d = 'Pythonc#JavaPc#HPc#'
# r = re.sub('c#',convert,d)
# print(r)

# def convert(value):
#     val = value.group()
#     return '888' if int(val) > 100 else '666'
#
# a = 'AB3CD18GHUB245IWEHN9551HF1UI454REM'
# r = re.sub('\d+',convert,a)
# print(a+"\n"+r)

# a = 'life not is,java and python'
# r = re.search('life(.*)python',a)
# r1 = re.findall('life(.*)python',a)
# print(r.group(1))
# print(r1)


# class DataExcel1:

# def test_001(self):
# wb  = xlrd.open_workbook(os.path.join(DATA_DIR, 'LoginC噩噩女ase.xlsx'))
# sheets = wb.get_sheet('测试案例')
# new_wb = copy(wb)
# new_wb
# actual_cell = write_ws.cell(2, 10, 'aaaaaaaaaaaaa')
# write_wb.save('测试案例')
# print()

# def test_002(self):
#     file_name = os.path.join(DATA_DIR, 'CaseEntity.xlsx')
#     try:
#         case = openpyxl.open(file_name)
#         sheet_active = case[Config().get_value('sheet', 'isrun')]
#         sheet_active.cell(5, 12, '66666666666')
#         case.save(file_name)
#     except FileNotFoundError:
#         Log.get_log().info('文件不存在')
#     except PermissionError:
#         Log.get_log().info('文件已经打开，不能写入')


# print(Student._Student__name)

# def function(a,*args,**kwargs):
#     print(type(a))
#     print(type(args))
#     print(type(kwargs))
# function('2',2,2,2,2,34,54,s=1,n=2)


# def a1():
#     for i in range(1,5):
#         return i
# def a2():
#     for i in range(1,5):
#         yield i
#
# print(a1())
# print(a2())
# s = a2()
# for i in s:
#     print(i)

# a = [1,2,3,4,5,65,7,8,9]
# s = map(lambda x: x*x,a)
# print(list(s))
# b = [i*i for i in a]
# print(b)
# c = [i*i for i in a if i >2]
# print(c)
# s = {'key1':1,'key2':2,'key3':3}
# s1 = [key for key,value in s.items()]
# print(s1)

# def quick_sort(s):
#     if s ==[]:
#         return []
#     first = s[0]
#     left = quick_sort([_ for _ in s[1:] if _ < first])
#     right = quick_sort([_ for _ in s[1:] if _ >= first])
#     return left +[first]+right
# s = [9,6,8,3,4,52,63,98]
# print(quick_sort(s))

# def mp_sort(s):
#     count = len(s)
#     for i in range(0,count):
#         for j in range(i+1,count):
#             if s[i] > s[j]:
#                 s[i],s[j] = s[j],s[i]
#     return s
# s = [9,6,8,3,4,52,63,98]
# print(mp_sort(s))
# class Student:
#     name = "扎马斯"
#     def a(self): #实例方法，需要用实例来调用
#         self.name = '1111'
#         print(self.name)
#
#     @classmethod
#     def b(cls):   #类方法，类直接调用，可以调用类变量
#         print(cls.name)
#
#     @staticmethod
#     def d():   #类方法，类直接调用，可以调用类变量
#         print("dddddd")
#
#     def __get(self): #私有方法
#         print("_____")
# from functools import wraps
#
# class abc:
#     def logs(func):
#         @wraps(func)
#         def warps_func(**kwargs):
#             print(kwargs)
#             func(**kwargs)
#         return warps_func
#
#     def run_main(self, **kwargs):
#         res = None
#         if kwargs.get('method') == "post":
#             res = self.http_post(**kwargs)
#         else:
#            pass
#
#     @logs
#     def http_post(**kwargs):
#         res = None
#         if kwargs.get('header') is not None:
#             pass
#         else:
#             pass
#
# abc().run_main(url='111', method='2222', case='33', header='444')
# # print('=========')
# from jsonpath_ng import jsonpath,parse
# import json
#
# a = {"case": {
#     "code": "200",
#     "person": [
#       {
#         "age": "23ccc",
#         "id": "23",
#         "name": "qqqq"
#       },
#       {
#         "age": "25www",
#         "dependid": 888888888888888900000,
#         "id": "22"
#       }
#     ]
#   }
# }
# case = json.loads(json.dumps(a))
# jsonpath_expr = parse('$.case.person[*].name')
# jsonpath_expr.find(case)
# jsonpath_expr.update(case, "22222")
# print(json.dumps(case, indent=2))


# print(jsonpath(a,"$.case.person[*].name"))

# from common.get_json import *
#
# # print(JsonData.get_key('test005'))
# a = {'a':1,'b':2}
# print(a)
# a.update({'a':5555555555})
# print(a)


# for i in range(1, 6 + 1):
#     print(i)
# from common.get_config import Config
# from common.get_data import GetData
# from common.log import Log
# from common.get_excel import ExcelData
# from functools import wraps
#
#
# class A:
#     def _init(func):
#         @wraps(func)
#         def inner_func(self):
#             self.data = GetData(Config().get_value('sheet', 'isRun'))
#             self.count = self.data.get_lines()
#             self.log = Log.get_log()
#             self.excel = ExcelData()
#             func(self)
#         return inner_func
#
#     @_init
#     def test_module1(self):
#         ''''''
#         print(self.count)
#
#
# A().test_module1()
# print(a.count)

# from os
# def exites:
#     os.path.exists(“goal”)

# from common.setting import REPORT_DIR_PATH
# import os
# import shutil
#
# def exists():
#     file_path = REPORT_DIR_PATH+r'\\report.html'
#     if os.path.exists(file_path):
#         os.remove(file_path)
# exists()
# import unittest
# from module.base import TestObject
#
# class TestCaseM000(TestObject,unittest.TestCase):
#     def __init__(self,i):
#         self.name = 'iiiiiiiiiii'
#         # pass
#         print(i)
#
# class TestCaseM001(TestCaseM000):
#     def __init__(self,i):
#        print(i)
#        TestCaseM000.__init__(self,i)
#
#     def a(self):
#         print(self.name)
#
#
# a = TestCaseM001('4444')
# print(a.a())
from functools import wraps
import unittest


class A(unittest.TestCase):

    def _init(func):
        @wraps(func)
        def inner_func(self, args):
            print(f"======================{args}")
            func(self, args)

        return inner_func

    @_init(8)
    def test_a(self, i: int = 1):
       print("----------------------")

if __name__ == '__main__':
    unittest.main()

