#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging
import datetime
import os


class MyLog:

    _instance = None

    def __init__(self):
        self.my_logger = logging.getLogger("ssbai")
        self.my_logger.setLevel(logging.DEBUG)
        today = datetime.datetime.today().date()
        self.log_path = r"C:\Users\ssbai\PycharmProjects\pythonProject\ui_test\logs\{0}".format(today)
        self.filename = "{0}/{1}.log".format(self.log_path, today)
        self.create_file()
        self.write_log()

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
        else:
            return cls._instance

    def create_file(self):
        if os.path.exists(self.log_path) is False:
            os.makedirs(self.log_path)

    def write_log(self):
        f = logging.FileHandler(self.filename, "a+", encoding="utf-8")
        f.setLevel(logging.DEBUG)
        fmt2 = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line -"
                                     " %(message)s", datefmt="%Y/%m/%d %H:%M:%S")
        f.setFormatter(fmt2)
        self.my_logger.handlers = []
        self.my_logger.addHandler(f)

    def debug(self, msg):
        self.my_logger.debug(msg)

    def info(self, msg):
        self.my_logger.info(msg)

    def error(self, msg):
        self.my_logger.error(msg)

    def warning(self, msg):
        self.my_logger.warning(msg)

    def critical(self, msg):
        self.my_logger.critical(msg)


if __name__ == '__main__':
    MyLog().debug('debug message')
    MyLog().info('info message')
    MyLog().warning('warn message')
    MyLog().error('error message')
    MyLog().critical('critical message')
