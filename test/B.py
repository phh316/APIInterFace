#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/14
# @Author : Ph
# # @File : B.py
# import unittest
#
# class A(unittest.TestCase):
#
#     def __init__(self):
#         print('---------------')
#         self.i = 0
#
# if __name__ == '__main__':
#     print('==========')
#     unittest.main()

# def get_parameter(*args, **kwargs):  # 工厂函数，用来接受@get_parameter('index.html/')的'index.html/'
#     def log_time(func):
#         def make_decorater():
#             print(args, kwargs)
#             func()
#         return make_decorater
#     return log_time
#
#
# @get_parameter('index.html/')
# def test():
#     pass
# # test()
# import unittest
# class A(unittest.TestCase):
#
#     def out_func(**kwargs):
#         def _init(func):
#             def inner_func(self):
#                 print(kwargs.get('i'))
#                 func(self)
#             return inner_func
#         return _init
#
#     @out_func(i = '4444')
#     def test_a(self):
#         pass
#
# class A1():
#
#     def out_func(**kwargs):
#         def _init(func):
#             def inner_func(self):
#                 print(kwargs.get('i'))
#                 func(self)
#             return inner_func
#         return _init
#
# if __name__ == '__main__':
#     unittest.main()
# from common.get_config import Config
# a = Config().get_value('sheet', 'run_module').split(',')[0]
# print(a)

