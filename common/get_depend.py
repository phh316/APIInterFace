# -*- coding: utf-8 -*-
from common.get_config import Config
from common.get_json import JsonData
from main.apimain import ApiRunner
from common.get_excel import ExcelData
from common.get_data import GetData
from jsonpath import jsonpath
from common.log import Log
import json


class DependData:

    def __init__(self,id):
        self.id = id
        self.log = Log.get_log()
        self.excel = ExcelData()
        self.data = GetData(Config().get_value('sheet', 'isRun'))
        self.depend_id = int(Config().get_value('excel', 'dependentId'))
        self.depend_data = int(Config().get_value('excel','dependentData'))
        self.depend_para = int(Config().get_value('excel','dependentPara'))

    def get_case_id_data(self, id):
        """
        调用excel的方法
        :param id:
        :return:
        """
        return self.excel.get_row_id_data(self.id)

    def get_depend_data(self,row):
        """
        获取excel中的依赖数据列
        :param row:
        :return:
        """
        data = self.excel.get_value(row, self.depend_para)
        return data if data is not None else None

    def get_depend_id_data(self,row):
        """
        获取excel中的依赖数据列
        :param row:
        :return:
        """
        data = str(self.excel.get_value(row, self.depend_data))
        data = data.split(',')
        return data


    def run_depend_id(self):
        """
        执行
        :return:
        """
        runner = ApiRunner()
        row_num = self.excel.get_row_num_depend_id(self.id)
        request_name = self.data.get_name(row_num)
        request_url = self.data.get_url(row_num)
        a = self.data.get_data(row_num)
        request_data = JsonData().get_key(self.data.get_data(row_num))
        request_method = self.data.get_method(row_num)
        request_header = self.data.get_header(row_num)
        self.log.info("[name] : {} [url] :{} [case] :{} [method] {} [header] {}"
                      .format(request_name, request_url, request_data, request_method, request_header))
        res = runner.run_main(request_url, request_method, request_data, request_header)
        return json.loads(res)

    def get_data_for_key(self, row):
        """
        获取依赖的返回数据
        :param row:
        :return:
        """
        result = []
        depend_data = str(self.get_depend_data(row))
        response_data = self.run_depend_id()
        data_list = depend_data.split(',')
        for item in data_list:
            result.append(jsonpath(response_data,item)[0])
        return result


