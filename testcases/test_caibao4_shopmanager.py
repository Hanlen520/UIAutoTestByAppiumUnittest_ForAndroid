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
import os
from api.user_activate_login import user_login, user_logout3, merchant_activate


class ShopManagerLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # super(MerchantActivateAndLogin, cls).setUpClass()
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "48decad2"
        caps["appActivity"] = "com.ziyuanpai.caibao.MainActivity"
        caps["appPackage"] = "com.ziyuanpai.caibao"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        content = util.load_yaml_file(os.getcwd() + '/config/merchant_VIP.yml')
        merchant_info = content.get('MerchantInfo')
        manager_info = content.get('ShopManagerInfo')
        cls.merchant_code = merchant_info['merchant_code']
        cls.user_code = manager_info['usercode']
        cls.password = manager_info['password']

        merchant_activate(cls.driver, cls.merchant_code)

    @classmethod
    def tearDownClass(cls):
        # super(MerchantActivateAndLogin, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        user_login(self.driver, self.user_code, self.password)

    def tearDown(self):
        user_logout3(self.driver)

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '重新激活'), 'Not log out')

    def test_find_element_index(self):
        # 店长登录成功之后，首页的页面元素
        text_list = ['收款', '会员列表', '商品收银', '交易分析', '我的二维码', '收款金额', '新注册会员',
                     '采宝', '账本', '活动', '我的']

        for each in text_list:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

    def test_find_element_receive_money(self):
        # 店长登录成功之后，收款页面元素
        util.find_textview_by_xpath_and_click(self.driver, '收款')

        text_list = ['快捷收银', '商品收银', '去收款', '添加不参与优惠金额', '删除', '清空']

        for each in text_list:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        els1 = self.driver.find_element_by_xpath("//android.widget.EditText[@text='输入金额']")
        self.assertIsNotNone(els1)
        self.driver.back()

    def test_vip_list_search(self):

        WebDriverWait(self, 20).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员列表']"))

        util.find_textview_by_xpath_and_click(self.driver, '会员列表')

        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='搜索会员']"))

        util.find_edittext_by_xpath_and_sendkeys(self.driver, '输入会员手机号搜索', '18621902561')

        self.driver.press_keycode(util.KEYCODE_ENTER)

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '为您找到1个结果'), 'Not find a vip')

        self.driver.back()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(MerchantActivateAndLogin)

    suite = unittest.TestSuite()

    # 收银员登录
    suite.addTest(ShopManagerLogin("test_find_element_index"))
    suite.addTest(ShopManagerLogin("test_find_element_receive_money"))
    suite.addTest(ShopManagerLogin("test_vip_list_search"))

    unittest.TextTestRunner(verbosity=2).run(suite)

