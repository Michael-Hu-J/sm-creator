# -*- coding:utf-8 -*-
import os.path
import time
import base64

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from creator.core.CreatorDriver import MobileCreatorDriver
from creator.core.android.GetDriver import android_dir


class AndroidCreatorDriver(MobileCreatorDriver):
    def __init__(self, driver):
        self.driver = driver

    def press(self, keycode=None):
        """
        模拟Android键盘按键
        导入appium.webdriver.extensions.android.nativekey.AndroidKey
        :param keycode: 使用类似AndroidKey.HOME
        :return: 无
        """
        self.driver.press_keycode(keycode)

    def save_screenshot(self, description=None):
        """
        截图并存入文件夹
        :param description: 截图描述
        :return:
        """
        screenshot_path = os.path.join(android_dir, "screenshots/{}_{}.png".format(description,
                                                                                   time.strftime("%Y-%m-%d",
                                                                                                 time.localtime())))
        self.driver.get_screenshot_as_file(screenshot_path)

    def start_screenrecord(self):
        self.driver.start_recording_screen()

    def stop_screenrecord(self, description=None):
        record = self.driver.stop_recording_screen()
        record_path = os.path.join(android_dir, "record/{}_{}.mp4".format(description,
                                                                          time.strftime("%Y-%m-%d",
                                                                                        time.localtime())))
        with open(record_path, mode="wb+") as r:
            r.write(base64.b64decode(record))

    def findElement(self, by=AppiumBy.ID, value=None):
        """
        导入from appium.webdriver.common.appiumby import AppiumBy
        :param by: AppiumBy.ID, AppiumBy.ACCESSIBILITY_ID, AppiumBy.CLASS_NAME, AppiumBy.NAME, AppiumBy.XPATH, AppiumBy.IMAGE, AppiumBy.ANDROID_UIAUTOMATOR
        :param value: 属性值
        :return:
        """
        return self.driver.find_element(by, value)

    def findElements(self, by=AppiumBy.ID, value=None):
        """
        导入from appium.webdriver.common.appiumby import AppiumBy
        :param by: AppiumBy.ID, AppiumBy.ACCESSIBILITY_ID, AppiumBy.CLASS_NAME, AppiumBy.NAME, AppiumBy.XPATH, AppiumBy.IMAGE, AppiumBy.ANDROID_UIAUTOMATOR
        :param value: 属性值
        :return: 返回一个list
        """
        return self.driver.find_elements(by, value)

    def wait_element_explicit(self, by=AppiumBy.ID, value=None, wait_time=5):
        """
        导入from appium.webdriver.common.appiumby import AppiumBy
        :param by: AppiumBy.ID, AppiumBy.ACCESSIBILITY_ID, AppiumBy.CLASS_NAME, AppiumBy.NAME, AppiumBy.XPATH, AppiumBy.IMAGE, AppiumBy.ANDROID_UIAUTOMATOR
        :param value: 属性值
        :param wait_time: 最长等待事件，默认5秒
        :return:
        """
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((by, value)))

    def wait_elements_explicit(self, by=AppiumBy.ID, value=None, wait_time=5):
        """
        导入from appium.webdriver.common.appiumby import AppiumBy
        :param by: AppiumBy.ID, AppiumBy.ACCESSIBILITY_ID, AppiumBy.CLASS_NAME, AppiumBy.NAME, AppiumBy.XPATH, AppiumBy.IMAGE, AppiumBy.ANDROID_UIAUTOMATOR
        :param value: 属性值
        :param wait_time: 最长等待事件，默认5秒
        :return: 返回一个list
        """
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_all_elements_located((by, value)))

    def quit(self):
        self.driver.quit()

    @property
    def contexts(self):
        """
        获取当前contexts
        :return: 返回list
        """
        return self.driver.contexts

    @property
    def current_context(self):
        """
        获取当前context
        :return:
        """
        return self.driver.current_context

    def tap(self, positions, duration=None):
        """
        模拟手指点击，一般页面元素难以定位时使用
        :param positions: 坐标值，最多五组，格式：List[Tuple[int, int]]，如：[(100, 20), (100, 60)]
        :param duration: 持续事件，单位毫秒
        :return:
        """
        self.driver.tap(positions=positions, duration=duration)

    def scroll(self, origin_el, destination_el, duration=None):
        """
        从一个元素滚动到另一个元素
        :param origin_el: 开始要滚动的元素，使用findElement()方法的返回值
        :param destination_el: 要滚动到的元素，使用findElement()方法的返回值
        :param duration: 持续时间，从原始元素到目标元素的滚动操作速度，单位毫秒，duration=None时，默认时600ms
        :return:
        """
        self.driver.scroll(origin_el=origin_el, destination_el=destination_el, duration=duration)

    def is_app_installed(self, app_info):
        pass

    def install_app(self, app_info):
        pass

    def remove_app(self, app_info):
        pass

    def launch_app(self):
        self.driver.activate_app("com.shinemo.baas.shinemo")

    def close_app(self):
        pass

    def shake(self):
        pass

    def maximize_window(self):
        pass

    def refresh(self):
        pass
