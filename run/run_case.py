# -*- coding: utf-8 -*-

from main.api_runner import ApiRunner
from common.get_json import JsonData
from common.get_depend import DependData
from jsonpath_ng import parse
import sys
import os
import json

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class RunTest():

    def __init__(self, **kwargs):
        self.run = ApiRunner()
        self.data = kwargs.get('data')
        self.log = kwargs.get('log')

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
                depend_data_id = DependData(id=depend_data)
                for v1, v2 in zip(depend_data_id.get_data_for_key(i), depend_data_id.get_depend_id_data(i)):
                    json_expr = parse(v2)
                    json_expr.find(data)
                    self.log.info(f"匹配规则为 :{json_expr} 匹配到的value为 :{v1}")
                    json_expr.update(data, v1)
            res = self.run.run_main(url, method, data, header)
            return res
