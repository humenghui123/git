#! /usr/bin/env python
# -*- coding:utf8 -*-
'''
@Environment:python 2.7
@Version: V2.2
@File: Log.py
@Author: zhangguangde
@CreateTime: 18/8/29 下午16:21
@UpdateTime: 18/8/29 下午16:21
@Description:
'''

import logging
import random
from logging.handlers import RotatingFileHandler

class Logger(logging.Logger):
    def __init__(self, level=logging.INFO, logfile=None):
        self.logger = logging.getLogger('__name__.{}'.format(random.random()))
        self.logger.setLevel(level)
        self.log_console(level)
        if logfile is not None:
            level = logging.DEBUG
            self.logger.setLevel(level)
            self.log_file(logfile, level)

    def log_console(self, level=logging.INFO):
        self.hander = logging.StreamHandler()
        # self.fnt = '[aclog title=%(step_name)-8s time=%(asctime)s level=%(levelname)-8s] %(message)s'
        self.fnt = '[aclog title=%(step_name)s time=%(asctime)s level=%(levelname)s]%(message)s'
        formatter = logging.Formatter(self.fnt, datefmt='%Y%m%d%H%M%S')
        self.hander.setLevel(level)
        self.hander.setFormatter(formatter)
        self.logger.addHandler(self.hander)

    def log_file(self, logfile, level):
        #定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
        self.Rthandler = RotatingFileHandler(logfile, maxBytes=5*1024*1024, backupCount=5)
        self.fnt = '[aclog title=%(step_name)s time=%(asctime)s level=%(levelname)s]%(message)s'
        formatter = logging.Formatter(self.fnt, datefmt='%Y%m%d%H%M%S')
        self.Rthandler.setLevel(level)
        self.Rthandler.setFormatter(formatter)
        self.logger.addHandler(self.Rthandler)

    def get_logger(self):
        return self.logger