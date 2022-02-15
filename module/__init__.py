from common.log import Log
from common.get_excel import ExcelData
from common.get_excel import Config
from common.get_data import GetData


def out_func(i:int):
    def _init(func):
        def inner_func(self):
            self.data = GetData(Config().get_value('sheet', 'run_module').split(',')[i])
            self.count = self.data.get_lines()
            self.log = Log.get_log()
            self.excel = ExcelData(i=i)
            func(self)
        return inner_func
    return _init


