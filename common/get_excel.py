# -*- coding: utf-8 -*-
import openpyxl
import xlrd
from common.log import Log
from common.get_config import Config
from common.setting import DATA_DIR_PATH
import os

class ExcelData:

    def __init__(self, sheet_name=None,i:int = 0):
        """
        加载excel文件
        :return:
        """
        self.file_name = os.path.join(DATA_DIR_PATH, "CaseEntity.xlsx")
        self.is_default = Config().get_value('sheet', 'default')
        self.is_run = Config().get_value('sheet', 'run_module').split(',')[i]
        self.data = self.get_sheet(sheet_name)
        self.log = Log.get_log()

    def get_nrows(self):
        """
        返回总行数
        :return:
        """
        return self.data.nrows

    def get_sheet(self, sheet_name=None):
        """
        加载sheet内容
        :return:
        """
        data = xlrd.open_workbook( self.file_name )
        if sheet_name is None:
            return data.sheets()[int(self.is_default)]
        else:
            return data.sheet_by_name(sheet_name)

    def get_value(self, row=None, col=None):
        """
        获取单元格数据
        :param row: 行数
        :param col: 列数
        :return:
        """
        if row is None or col is None:
            self.log.info("获取单元格数据失败，参数[row]为 :  {},参数[col]为 :  {}".format(row, col))
        else:
            return self.data.cell_value(row, col)


    def wirte_value(self,row,value):
        """
        回写excel数据
        :param row:
        :param col:
        :param value:
        :return:
        """
        try:
            data = openpyxl.open(self.file_name)
            sheet_active = data[self.is_run]
            sheet_active.cell(row+1,int(Config().get_value('excel', 'end')), value)
            data.save(self.file_name)
        except FileNotFoundError:
            Log.get_log().info('文件不存在')
        except PermissionError:
            Log.get_log().info('文件已经打开，不能写入')

    def get_row_id_data(self,depend_id):
        """
        通过depend_id获取对应行数据
        :param id:
        :return:
        """
        row_num = self.get_row_depend_id(depend_id)
        data = self.get_row_data(row_num)
        return data

    def get_row_num_depend_id(self,id):
        """
        通过dependid获取对应行号
        :param id:
        :return:
        """
        num = 1
        datas = self.get_col_data()
        for data in datas:
            if id == data:
                return num
            num += 1

    def get_row_data(self,row):
        """
        根据行号,获取该行内容
        :param row:
        :return:
        """
        return self.data.row_values(row) if row < self.get_nrows() else Log.get_log().info("数组越界")

    def get_col_data(self, col=None):
        """
        根据列号,获取该行内容
        :param col:
        :return:
        """
        return self.data.col_values(0,1) if col is None else self.data.col_values(col,1)


# if __name__ == '__main__':
#     exceldata = ExcelData()
#     print(exceldata.get_value(1,0))
