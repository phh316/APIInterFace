# -*- coding: utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from main.apimain import ApiRunner
from common.get_data import GetData
from common.get_json import JsonData
from common.log import Log
from common.get_config import Config
from common.get_excel import ExcelData
from common.get_depend import DependData
from jsonpath_ng import parse
import json


class RunTest():

    def __init__(self):
        self.log = Log.get_log()
        self.run = ApiRunner()
        self.data = GetData(Config().get_value('sheet', 'run_module1'))
        self.excel = ExcelData()

    def runner(self, i):
        is_run = self.data.get_is_run(i)
        if is_run:
            name = self.data.get_name(i)
            url = self.data.get_url(i)
            data = JsonData().get_key(self.data.get_data(i))
            data = json.loads(json.dumps(data))
            method = self.data.get_method(i)
            header = self.data.get_header(i)
            depend_data = self.data.is_depend(i)
            if depend_data:
                self.log.info("[name] : {} [url] :{} [is_run] :{} [case] :{} [method] {} [header] {}"
                              .format(name, url, is_run, data, method, header))
                self.depend_data_id = DependData(depend_data)
                for v1,v2 in zip(self.depend_data_id.get_data_for_key(i),self.depend_data_id.get_depend_id_data(i)):
                    json_expr = parse(v2)
                    json_expr.find(data)
                    self.log.info(f"匹配规则为 :{json_expr} 匹配到的value为 :{v1}")
                    json_expr.update(data, v1)
            res = self.run.run_main(url, method, data, header)
            return res
