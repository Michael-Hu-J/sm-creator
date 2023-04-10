# -*- coding:utf-8 -*-
from abc import ABC, abstractmethod


class CreatorDriver(ABC):

    def __int__(self):
        pass

    @abstractmethod
    def press(self):
        pass

    @abstractmethod
    def save_screenshot(self):
        pass

    @abstractmethod
    def start_screenrecord(self):
        pass

    @abstractmethod
    def stop_screenrecord(self):
        pass

    @abstractmethod
    def findElement(self):
        pass

    @abstractmethod
    def quit(self):
        pass


class MobileCreatorDriver(CreatorDriver):

    def __int__(self):
        pass

    @abstractmethod
    def contexts(self):
        pass

    @abstractmethod
    def current_context(self):
        pass

    @abstractmethod
    def tap(self, positions, duration=None):
        pass

    @abstractmethod
    def scroll(self, origin_el, destination_el):
        pass

    @abstractmethod
    def is_app_installed(self, app_info):
        pass

    @abstractmethod
    def install_app(self, app_info):
        pass

    @abstractmethod
    def remove_app(self, app_info):
        pass

    @abstractmethod
    def launch_app(self):
        pass

    @abstractmethod
    def close_app(self):
        pass

    @abstractmethod
    def shake(self):
        pass


class PcCreatorDriver(CreatorDriver):

    def __int__(self):
        pass

    @abstractmethod
    def startApp(self):
        pass

    @abstractmethod
    def closeApp(self):
        pass

    @abstractmethod
    def closeApp(self):
        pass

    @abstractmethod
    def is_process_running(self):
        pass

    @abstractmethod
    def getTopWindow(self):
        pass

    @abstractmethod
    def maximize_window(self):
        pass
