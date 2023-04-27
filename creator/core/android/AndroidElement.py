# -*- coding:utf-8 -*-

from appium.webdriver.common.appiumby import AppiumBy
from creator.core.BaseElement import BaseElement
from creator.core.android.AndroidCreatorDriver import AndroidCreatorDriver


class AndroidELement(BaseElement, AndroidCreatorDriver):
    def click(self, by=AppiumBy.ID, value=None):
        super().findElement(by=by, value=value).click()

    def send_keys(self, by=AppiumBy.ID, value=None, send_value=None):
        self.click(by=by, value=value)
        super().findElement(by=by, value=value).clear()
        super().findElement(by=by, value=value).send_keys(send_value)

    def text(self, by=AppiumBy.ID, value=None):
        return super().findElement(by=by, value=value).text
