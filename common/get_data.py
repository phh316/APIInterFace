# -*- coding: utf-8 -*-
from common.get_excel import ExcelData
from common.get_json import JsonData
from common.setting import HEADER
from common.get_config import Config


class GetData:

    def __init__(self, sheet_name=None):
        self.excel = ExcelData(sheet_name)
        self.depend_id = int(Config().get_value('excel','dependentId'))

    def get_lines(self):
        """
        获取行数
        :return:
        """
        return self.excel.get_nrows()

    def get_is_run(self, row):
        """
        是否执行
        :param row:
        :return:
        """
        col = int(Config().get_value('excel','isRun'))
        is_run = self.excel.get_value(row, col)
        if is_run == 'yes':
            return True
        else:
            return False

    def get_header(self, row):
        """
        是否携带header
        :param row:
        :return:
        """
        col = int(Config().get_value('excel', 'header'))
        header = self.excel.get_value(row, col)
        if header == 'yes':
            return self.get_header_value()
        else:
            return None

    def get_method(self, row):
        """
        获取请求方式
        :param row:
        :return:
        """
        col = int(Config().get_value('excel', 'method'))
        return self.excel.get_value(row, col)

    def get_url(self, row):
        """
        获取url
        :param row:
        :return:
        """
        col = int(Config().get_value('excel', 'url'))
        return self.excel.get_value(row, col)

    def get_name(self, row):
        """
        获取url
        :param row:
        :return:
        """
        col = int(Config().get_value('excel', 'name'))
        return self.excel.get_value(row, col)

    def get_data(self, row):
        """
        获取请求数据
        :param row:
        :return:
        """
        col = int(Config().get_value('excel', 'case'))
        return ' ' if self.excel.get_value(row, col) == '' else self.excel.get_value(row, col)

    def get_json(self, row):
        """
        获取jsonId
        :param row:
        :return:
        """
        return JsonData().get_key(self.get_data(row))

    def get_except_result(self, row):
        """
        获取预期结果
        :return:
        """
        col = int(Config().get_value('excel', 'exceptResult'))
        return ' ' if self.excel.get_value(row, col) == '' else self.excel.get_value(row, col)

    def get_header_value(self):
        """
        获取头信息
        :return:
        """
        return HEADER

    def is_depend(self, row):
        """
        判断是否存在依赖
        :param id:
        :return:
        """
        return \
            None if self.excel.get_value(row, self.depend_id) \
                    is None else \
                self.excel.get_value(row, self.depend_id)
