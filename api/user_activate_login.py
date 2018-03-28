#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     user_activate_login
   Description :
   Author :        Meiyo
   date：          2018/3/19 20:38
-------------------------------------------------
   Change Activity:
                   2018/3/19:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import util
from time import sleep


def merchant_activate(driver, merchant_code):

    driver.find_element_by_id("android:id/button1").click()

    # 引导页，左滑动屏幕
    util.swipe_to_left(driver)
    util.swipe_to_left(driver)
    util.swipe_to_left(driver)

    util.find_textview_by_xpath_and_click(driver, '立即体验')

    driver.find_element_by_xpath("//android.widget.EditText[@text='输入手机号/商户号']").send_keys(merchant_code)

    util.find_textview_by_xpath_and_click(driver, '激活')

    driver.find_element_by_id("android:id/button1").click()


def user_login(driver, usercode, password):
    # self.driver.implicitly_wait(2)

    # 商户登录
    driver.find_element_by_accessibility_id("login_user_code").send_keys(usercode)
    # el5 = driver.find_element_by_accessibility_id("login_user_code")
    # el5.send_keys(usercode)

    driver.find_element_by_accessibility_id("login_pwd_code").send_keys(password)
    # el6 = driver.find_element_by_accessibility_id("login_pwd_code")
    # el6.send_keys(password)
    driver.hide_keyboard()

    util.find_textview_by_xpath_and_click(driver, '登录')


def user_logout3(driver):
    sleep(1)
    # 打开 我的tab
    util.find_textview_by_xpath_and_click(driver, '我的')

    # 打开设置tab
    util.find_textview_by_xpath_and_click(driver, '设置')

    util.find_textview_by_xpath_and_click(driver, '退出登录')

    # 确认退出
    driver.find_element_by_id("android:id/button2").click()


def user_logout4(driver):
    sleep(1)

    # 打开 我的tab
    util.find_textview_by_xpath_and_click(driver, '我的')

    # 打开设置tab
    el2 = driver.find_element_by_accessibility_id("my_setting")
    el2.click()

    sleep(2)

    # 向上滑动
    util.swipe_to_up(driver)

    util.find_textview_by_xpath_and_click(driver, '退出登录')

    # 确认退出
    driver.find_element_by_id("android:id/button2").click()
