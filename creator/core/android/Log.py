#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
封装log方法
"""

import logging
import time
import os.path
from creator.core.android.GetDriver import android_dir

log_path = os.path.join(android_dir, "log/{}.log".format(time.strftime("%Y-%m-%d", time.localtime())))


class MyLog:
    def __init__(self, name=__name__, path=log_path, level=logging.DEBUG):
        self.__name = name
        self.__path = path
        self.__level = level
        self.__logger = logging.getLogger(self.__name)  # 初始化logger
        self.__logger.setLevel(self.__level)  # 设置基础log等级为debug，debug优先级最低
        self.__logger.handlers.clear()  # 清理已存在的handlers，避免日志重复打印

    # 初始化一个filehandler
    def __init_handler(self):
        handler = logging.FileHandler(self.__path)
        return handler

    # 设置filehandler的日志格式
    def __set_formatter(self, handler):
        formatter = logging.Formatter(fmt="%(levelname)s %(asctime)s %(name)s %(filename)s-第%(lineno)d行: %(message)s")
        handler.setFormatter(formatter)

    # 添加此filehandler到logger
    def __set_handler(self, handler):
        self.__logger.addHandler(handler)

    # 关闭handler
    def __close_handler(self, handler):
        handler.close()

    def Logger(self):
        handler = self.__init_handler()
        self.__set_formatter(handler)
        self.__set_handler(handler)
        self.__close_handler(handler)
        return self.__logger

    @classmethod
    def debug(cls, log_meg):
        cls().Logger().debug(log_meg)

    @classmethod
    def info(cls, log_meg):
        cls().Logger().info(log_meg)

    @classmethod
    def warning(cls, log_meg):
        cls().Logger().warning(log_meg)

    @classmethod
    def error(cls, log_meg):
        cls().Logger().error(log_meg)

    @classmethod
    def exception(cls, log_meg):
        cls().Logger().exception(log_meg)

    @classmethod
    def critical(cls, log_meg):
        cls().Logger().critical(log_meg)
