#!/usr/bin/python3
# -*- coding:utf-8 -*-
import yaml
import os.path
from appium import webdriver
import time

"""
读取android配置文件，封装driver
"""


android_dir = os.path.dirname(os.path.abspath(__file__))

android_yaml_path = os.path.join(android_dir, "AndroidConfig.yaml")


def baas_desired_caps():
    with open(android_yaml_path, encoding="utf-8") as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)  # 编码成python对象
        desired_caps = data["desired_caps_baas"]
        return desired_caps


def baas_driver():
    desired_caps = baas_desired_caps()
    # print(desired_caps)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    return driver

# baas_driver()
