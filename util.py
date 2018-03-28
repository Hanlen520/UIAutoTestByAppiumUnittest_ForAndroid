#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     util
   Description :
   Author :        Meiyo
   date：          2018/3/19 20:39
-------------------------------------------------
   Change Activity:
                   2018/3/19:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import yaml
import io
import logging

# 参考https://developer.android.com/reference/android/view/KeyEvent.html
KEYCODE_ENTER = 66

def check_format(file_path, content):
    """ check testcase format if valid
    """
    if not content:
        # testcase file content is empty
        err_msg = u"Testcase file content is empty: {}".format(file_path)
        logging.error(err_msg)
        raise FileNotFoundError(err_msg)

    elif not isinstance(content, (list, dict)):
        # testcase file content does not match testcase format
        err_msg = u"Testcase file content format invalid: {}".format(file_path)
        logging.error(err_msg)
        raise FileNotFoundError(err_msg)


def load_yaml_file(yaml_file):
    """ load yaml file and check file content format
    """
    with io.open(yaml_file, 'r', encoding='utf-8') as stream:
        yaml_content = yaml.load(stream)
        check_format(yaml_file, yaml_content)
        return yaml_content


def swipe_to_left(driver, duration=None):
    try:
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')

        driver.swipe(width/6*5, height/2, width/6, height/2, duration)

    except Exception as ex:
        print(ex)


def swipe_to_up(driver, duration=None):
    try:
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')

        driver.swipe(width/2, (height/6)*5, width/2, height/6, duration)

    except Exception as ex:
        print(ex)


def find_textview_by_xpath_and_click(driver, name):
    try:
        els = driver.find_element_by_xpath("//android.widget.TextView[@text=\'" + name + "\']")
        if isinstance(els, list):
            els[0].click()
        else:
            els.click()

    except Exception as ex:
        print(ex, name)


def is_textview_exist_by_xpath(driver, name):
    try:
        els = driver.find_element_by_xpath("//android.widget.TextView[@text=\'" + name + "\']")
        if isinstance(els, list):
            return els[0].is_displayed()
        else:
            return els.is_displayed()
    except Exception as e:
        print(e, name)
        return False


def find_edittext_by_xpath_and_sendkeys(driver, name, value):
    try:
        els = driver.find_elements_by_xpath("//android.widget.EditText[@text=\'" + name + "\']")
        if isinstance(els, list):
            els[0].send_keys(value)
        else:
            els.send_keys(value)
    except Exception as ex:
        print(ex)


