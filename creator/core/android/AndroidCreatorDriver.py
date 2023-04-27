# -*- coding:utf-8 -*-
import os.path
import time
import base64

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from creator.core.CreatorDriver import MobileCreatorDriver
from creator.core.android.GetDriver import android_dir
from creator.core.android.Log import MyLog


class AndroidCreatorDriver(MobileCreatorDriver):
    def __init__(self, driver):
        self.driver = driver

    def press(self, keycode=None):
        """
        模拟Android键盘按键
        导入appium.webdriver.extensions.android.nativekey.AndroidKey
        :param keycode: 如：AndroidKey.HOME
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
        """
        开始屏幕录制
        :return: 如果在之前的“start_recording_screen”之后没有调用“stop_recording_screen”，返回为空字符串
        """
        self.driver.start_recording_screen()

    def stop_screenrecord(self, description=None):
        """
        结束屏幕录制
        :param description: 录制文件描述
        :return: bytes: 录制媒体的Base-64 编码内容
        """
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
        """
        关闭驱动连接
        :return:
        """
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
        :return: str，返回当前的context session
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
        """
        :param app_info: android包名，如："com.shinemo.baas.shinemo"
        :return: 返回 True 代表改包已安装，False 则反之
        """
        return self.driver.is_app_installed(app_info)

    def install_app(self, app_info, **options):
        """
        :param app_info: android安装包的名字，如："app.apk"
        :param options:
        Keyword Args:
            replace (bool): 是否重新安装/升级软件。默认是True
            timeout (int): 等待安装完成时间。默认是60000ms
            allowTestPackages (bool): 是否允许安装被标记为测试的包。默认是是False
            useSdcard (bool): 是否使用SD卡安装。默认是False
            grantPermissions (bool): 在android 6+安装完成后，是否自动授权应用程序权限。默认是False
        :return:
        """
        package_path = os.path.join(android_dir, "android_package/app_info")
        self.driver.install_app(package_path, **options)

    def remove_app(self, app_info, **options):
        """
        :param app_info: android包名，如："com.shinemo.baas.shinemo"
        :param options:
        Keyword Args:
            keepData (bool): 卸载后是否保留应用程序数据和缓存。默认是False
            timeout (int): 等待卸载完成时间。默认是20000ms
        :return:
        """
        self.driver.remove_app(app_info, **options)

    def launch_app(self):
        """
        启动app
        :return:
        """
        self.driver.launch_app()

    def close_app(self):
        """
        关闭当前app
        :return:
        """
        self.driver.close_app()

    def shake(self):
        """
        摇动设备
        :return:
        """
        self.driver.shake()

