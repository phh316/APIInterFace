# -*- coding: utf-8 -*-
import requests
import json
from functools import wraps
from common.log import Log


class ApiRunner:

    def logs(func):
        @wraps(func)
        def wraps_func(self, **kwargs):
            Log.get_log().info("发送请求: \n [url] :{} \n [method] :{} \n [case] :{} \n [header] {}\n"
                               .format(kwargs.get('url'),
                                       kwargs.get('method'),
                                       kwargs.get('data'),
                                       kwargs.get('headers')))
            return func(**kwargs)
        return wraps_func

    @logs
    def http_post(**kwargs):
        '''
        POST
        :param url:
        :param data:
        :param header:
        :return:
        '''
        res = None
        if kwargs.get('headers') is not None:
            res = requests.post(kwargs.get('url'),kwargs.get('case'),kwargs.get('headers'))
        else:
            res = requests.post(kwargs.get('url'),kwargs.get('case'))
        return res.json()

    @logs
    def http_get(**kwargs):
        '''
        get
        :param url:
        :param data:
        :param header:
        :return:
        '''
        res = None
        if kwargs.get('headers') is not None:
            res = requests.get(kwargs.get('url'),kwargs.get('case'),kwargs.get('headers'))
        else:
            res = requests.get(kwargs.get('url'),kwargs.get('case'))
        return res.json()

    def run_main(self, url, method, data, header):
        """
        主函数
        :param url:
        :param method:
        :param data:
        :param header:
        :return:
        """
        res = None
        if method == "post":
            res = self.http_post(url=url, method=method, data=data, headers=header)
        else:
            res = self.http_get(url=url, method=method, data=data)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
