# -*- coding: utf-8 -*-
import os
from common.setting import BASE_INI_PATH
from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self):
        """
        初始化
        """
        self.config_name = BASE_INI_PATH
        super().__init__()
        super().read(self.config_name,encoding='utf-8')


    def get_value(self,nodename,key):
        '''
        :param nodename: 节点名称
        :param key: key
        :return: 父类的get()
        '''
        if nodename!=None and key!=None:
            return super().get(nodename,key)
        else:
            print("传入参数[nodename]为 :  {},参数[key]为 :  {}".format(nodename, key))
            #self.Hlog.info("传入参数[nodename]为 :  {},参数[key]为 :  {}".format(nodename, key))

    def save_value(self,nodename,key,value):
        '''
        写入配置文件
        :param nodename: 节点名称
        :param key: key
        :param value: value
        :return: 父类set()
        '''
        if nodename!=None and key!=None and value!=None:
            super().set(section=nodename,option=key,value=value)
            super().write(fp = open(self.config_name,'w'))
        else:
            print("传入参数[nodename]为 :  {},参数[key]为 :  {},参数[value]为 :  {}".format(nodename,key,value))
            #self.log.info("传入参数[nodename]为 :  {},参数[key]为 :  {},参数[value]为 :  {}".format(nodename,key,value))

    def get_all_sections(self):
        """
        获取所有配置信息
        :return:
        """
        return super().sections()

    def get_option(self,nodename):
        """
        获取所有节点的key
        :param nodename:
        :return:
        """
        return super().options(nodename)

    def get_items(self,nodename):
        """
        获取所有节点的value
        :param nodename:
        :return:
        """
        return super().items(nodename)


# if __name__ == '__main__':
#     config = Config()
#     a = config.get_value('excel','isRun')
#     int(a)
#     print(type(int(a)))