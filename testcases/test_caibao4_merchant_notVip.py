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
from api.user_activate_login import merchant_activate, user_login, user_logout4
import os


class MerchantActivateAndLoginNotVip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # super(MerchantActivateAndLogin, cls).setUpClass()
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "192.168.24.101:5555"
        caps["appActivity"] = "com.ziyuanpai.caibao.MainActivity"
        caps["appPackage"] = "com.ziyuanpai.caibao.d"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)

        content = util.load_yaml_file(os.getcwd() + '/config/merchant_notVIP.yml')
        merchant_info = content.get('MerchantInfo')
        cls.merchant_code = merchant_info['merchant_code']
        cls.password = merchant_info['password']

        merchant_activate(cls.driver, cls.merchant_code)

    @classmethod
    def tearDownClass(cls):
        # super(MerchantActivateAndLogin, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):

        user_login(self.driver, self.merchant_code, self.password)

    def tearDown(self):
        user_logout4(self.driver)

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '重新激活'), 'Not log out')

    def test_01_close(self):

        WebDriverWait(self, 40).until(lambda x:
                                  self.driver.find_element_by_xpath("//android.widget.TextView[@text='我知道了']"))
        util.find_textview_by_xpath_and_click(self.driver, '我知道了')

    def test_find_element_today(self):

        # 商户登录成功之后，首页的页面元素
        text_list = ['今日交易额（账本）', '去收款', '收款笔数', '充值金额', '新增会员', '（未开通会员）', '查看盈亏',
                     '会员招募', '群体发券', '充值送礼', '累充送礼',
                     '今日', '会员', '消息', '我的']

        for each in text_list:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        util.find_textview_by_xpath_and_click(self.driver, '群体发券')

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '立即开始'))

        util.find_textview_by_xpath_and_click(self.driver, '立即开始')

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '申请试用'))

        self.driver.back()

    def test_find_element_today_report(self):

        WebDriverWait(self, 40).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='查看盈亏']"))

        util.find_textview_by_xpath_and_click(self.driver, '查看盈亏')

        # 商户登录成功之后，首页的页面元素
        text_list1 = ['交易金额', '订单笔数(笔)', '新增会员(人)', '充值金额(元)',
                     '消费金额渠道占比', '退款情况']

        for each in text_list1:
                self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        util.swipe_to_up(self.driver)

        text_list2 = ['新老会员消费金额占比', '24h交易金额走势图']

        for each in text_list2:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        self.driver.back()

    def test_find_element_vip(self):
        WebDriverWait(self, 40).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员']"))

        # 打开会员tab页面
        util.find_textview_by_xpath_and_click(self.driver, '会员')

        WebDriverWait(self, 40).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='开通会员管理功能']"))

        # 会员页的页面元素
        text_list = ['支付会员', '昨日新增(人)', '忠实用户', '七日回头率', '七日消费均单']

        for each in text_list:
                self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

    def test_find_element_Message(self):

        WebDriverWait(self, 60).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='消息']"))

        # 打开消息tab页面
        util.find_textview_by_xpath_and_click(self.driver, '消息')

        WebDriverWait(self, 60).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='消息中心']"))

        if util.is_textview_exist_by_xpath(self.driver, '平台活动'):
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='最新平台活动资讯']"))

        elif util.is_textview_exist_by_xpath(self.driver, '公告'):
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='官方公告']"))

        elif util.is_textview_exist_by_xpath(self.driver, '系统通知'):
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='系统反馈信息']"))

        elif util.is_textview_exist_by_xpath(self.driver, '数据报表'):
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='定期的运营数据推送']"))
        else:
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='您还没有新的消息']"))

    def test_find_element_Mine(self):
        WebDriverWait(self, 60).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']"))

        # 打开我的tab页面
        util.find_textview_by_xpath_and_click(self.driver, '我的')

        WebDriverWait(self, 60).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='门店']"))

        # 会员页的页面元素
        text_list1 = ['门店', '收银人员', '商品', '签约管理', '广告']

        for each in text_list1:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        util.swipe_to_up(self.driver)

        text_list2 = ['客服热线', '帮助中心']

        for each in text_list2:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        util.swipe_to_down(self.driver)


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(MerchantActivateAndLogin)

    suite = unittest.TestSuite()

    suite.addTest(MerchantActivateAndLoginNotVip("test_01_close"))

    # 首页测试
    suite.addTest(MerchantActivateAndLoginNotVip("test_find_element_today"))
    suite.addTest(MerchantActivateAndLoginNotVip("test_find_element_today_report"))
    #
    # # 会员页测试
    suite.addTest(MerchantActivateAndLoginNotVip("test_find_element_vip"))
    #
    # # 消息页面
    suite.addTest(MerchantActivateAndLoginNotVip("test_find_element_Message"))
    #
    # # 我的页面
    suite.addTest(MerchantActivateAndLoginNotVip("test_find_element_Mine"))

    unittest.TextTestRunner(verbosity=2).run(suite)

