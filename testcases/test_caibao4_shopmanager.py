#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     test_caibao4_merchant
   Description :
   Author :        Meiyo
   date：          2018/3/19 21:12
-------------------------------------------------
   Change Activity:
                   2018/3/19:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

from appium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
import util
from testsuit.user_login import test_user_login
import os
from time import sleep


class ShopManagerLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # super(MerchantActivateAndLogin, cls).setUpClass()
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "48decad2"
        caps["appActivity"] = "com.ziyuanpai.caibao.MainActivity"
        caps["appPackage"] = "com.ziyuanpai.caibao.d"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # super(MerchantActivateAndLogin, cls).tearDownClass()
        cls.driver.quit()

    def test_1_shop_manager_login(self):
        content = util.load_yaml_file(os.getcwd() + '/config/merchant_VIP.yml')
        merchant_info = content.get('MerchantInfo')
        shopmanager_info = content.get('ShopManagerInfo')
        merchant_code = merchant_info['merchant_code']
        user_code = shopmanager_info['usercode']
        password = shopmanager_info['password']

        test_user_login(self.driver, merchant_code, user_code, password)

    def test_2_find_element_index(self):
        # 店长登录成功之后，首页的页面元素
        text_list = ['收款', '会员列表', '商品收银', '交易分析', '商品', '我的二维码', '收款金额', '新注册会员',
                     '测试', '账本', '活动', '我的']

        try:
            for each in text_list:
                locator = "//android.widget.TextView[@text=\'" + each + "\']"
                els = self.driver.find_element_by_xpath(locator)
                WebDriverWait(self, 3).until(lambda x: els)
                self.assertIsNotNone(els)

        except Exception as ex:
            print(ex)

    def test_3_find_element_receive_money(self):
        # 店长登录成功之后，收款页面元素
        util.find_textview_by_xpath_and_click(self.driver, '收款')

        text_list = ['快捷收银', '商品收银', '去收款', '添加不参与优惠金额', '删除', '清空']

        try:
            for each in text_list:
                locator = "//android.widget.TextView[@text=\'" + each + "\']"
                els = self.driver.find_element_by_xpath(locator)
                WebDriverWait(self, 3).until(lambda x: els)
                self.assertIsNotNone(els)

        except Exception as ex:
            print(ex)

        els1 = self.driver.find_element_by_xpath("//android.widget.EditText[@text='输入金额']")
        self.assertIsNotNone(els1)

    def test_4_vip_list_search(self):

        self.driver.back()

        WebDriverWait(self, 20).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员列表']"))

        util.find_textview_by_xpath_and_click(self.driver, '会员列表')

        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='搜索会员']"))

        util.find_edittext_by_xpath_and_sendkeys(self.driver, '输入会员手机号搜索', '18621902561')

        self.driver.press_keycode(util.KEYCODE_ENTER)

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '为您找到1个结果'), 'Not find a vip')

    def test_5_shop_manager_logout(self):
        self.driver.back()

        # 打开 我的tab
        WebDriverWait(self, 20).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']"))
        util.find_textview_by_xpath_and_click(self.driver, '我的')

        # 打开设置tab
        util.find_textview_by_xpath_and_click(self.driver, '设置')

        util.find_textview_by_xpath_and_click(self.driver, '退出登录')

        # 确认退出
        WebDriverWait(self, 20).until(lambda x: self.driver.find_elements_by_id("android:id/buttonPanel"))
        self.driver.find_element_by_id("android:id/button2").click()

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '重新激活'), 'Not log out')


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(MerchantActivateAndLogin)

    suite = unittest.TestSuite()

    # 收银员登录
    suite.addTest(ShopManagerLogin("test_1_shop_manager_login"))
    suite.addTest(ShopManagerLogin("test_2_find_element_index"))
    suite.addTest(ShopManagerLogin("test_3_find_element_receive_money"))
    suite.addTest(ShopManagerLogin("test_4_vip_list_search"))
    suite.addTest(ShopManagerLogin("test_5_shop_manager_logout"))

    unittest.TextTestRunner(verbosity=2).run(suite)

