# -*- coding: utf-8 -*-
import logging
import os
from common.setting import LOG_DIR_PATH
from common.get_config import Config
from logging.handlers import TimedRotatingFileHandler


class Log:

    @staticmethod
    def get_log():
        level = Config().get_value('log', 'level')
        format = '%(asctime)s - %(name)s-%(levelname)s: %(message)s'
        logging.basicConfig(level=level, format=format)
        log = logging.getLogger('APIInterFace')
        file_name = os.path.join(LOG_DIR_PATH, 'log-out')
        f = TimedRotatingFileHandler(filename=file_name, when="D", backupCount=15, encoding='utf-8')
        f.setLevel(level)
        f.setFormatter(logging.Formatter(format))
        log.addHandler(f)
        return log
