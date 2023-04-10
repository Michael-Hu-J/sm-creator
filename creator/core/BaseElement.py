# -*- coding:utf-8 -*-
from abc import ABC, abstractmethod


class BaseElement(ABC):
    def __int__(self):
        pass

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def send_keys(self):
        pass

    @abstractmethod
    def text(self):
        pass