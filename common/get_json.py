# -*- coding: utf-8 -*-
import json
from common.setting import DATA_DIR_PATH
import os
from common.log import Log


class JsonData:

    def __init__(self):
        """
        初始化调用load_json函数
        """
        self.data = self.load_json()
        self.log = Log.get_log

    def load_json(self):
        """
        加载json文件
        :return:
        """
        with open(os.path.join(DATA_DIR_PATH, "dataJson.json"), encoding='utf-8') as f:
            return json.load(f)

    def get_key(self, id):
        """
        获取值
        :param id:
        :return:
        """
        json_data =None
        try:
            json_data = self.data[id]
        except KeyError:
            self.log().error("测试数据未定义")
        finally:
            return json_data
