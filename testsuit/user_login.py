#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     merchant_login
   Description :
   Author :        Meiyo
   date：          2018/3/19 20:51
-------------------------------------------------
   Change Activity:
                   2018/3/19:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

from api.user_activate_login import merchant_activate, user_login


def test_user_login(driver, merchant_code, user_code, password):
    merchant_activate(driver, merchant_code)
    user_login(driver, user_code, password)
