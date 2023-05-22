# from creator import __version__
#
#
# def test_version():
#     assert __version__ == '0.1.0'


# -*- coding:utf-8 -*-

import pytest
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from creator.core.android.AndroidCreatorDriver import AndroidCreatorDriver


@pytest.mark.usefixtures("driver")
class TestActivateApp:
    def test_activate_app(self, driver):
        AndroidCreatorDriver(driver).launch_app()
        time.sleep(3)
        # AndroidCreatorDriver(driver).press(AndroidKey.HOME)
        AndroidCreatorDriver(driver).save_screenshot(description="登录")
