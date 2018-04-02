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


class MerchantActivateAndLogin(unittest.TestCase):
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

        content = util.load_yaml_file(os.getcwd() + '/config/merchant_VIP.yml')
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
        text_list = ['今日交易额（账本）', '去收款', '收款笔数', '充值金额', '新增会员', '查看盈亏',
                     '会员招募', '群体发券', '充值送礼', '累充送礼',
                     '今日', '会员', '消息', '我的']

        for each in text_list:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

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
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='流失挽回']"))

        # 会员页的页面元素
        text_list = ['会员', '总会员', '价值', '普通', '沉睡', '流失', '上周数据',
                     '会员新增', '复购率', '流失率', '会员消费占比', '会员笔单价',
                     '招募会员', '增加黏性', '流失挽回']

        for each in text_list:
                self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

    def test_find_element_vip_vipList(self):
        # 打开会员列表页面
        el1 = self.driver.find_element_by_accessibility_id("vip_bar_right_bt")
        el1.click()

        self.assertTrue(util.is_textview_exist_by_xpath(self.driver, '输入会员手机号搜索'))

    def test_find_element_vip_marketing(self):
        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员']"))

        # 打开会员tab页面
        util.find_textview_by_xpath_and_click(self.driver, '会员')

        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='招募会员']"))

        util.find_textview_by_xpath_and_click(self.driver, '招募会员')

        # 会员招募
        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='招募方式']"))

        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='开卡送券']"))

        # 增加黏性
        util.swipe_to_left(self.driver)
        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='充值有礼']"))
        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='累充送礼']"))

        # 流失挽回
        util.swipe_to_left(self.driver)
        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='群体发券']"))

        self.driver.back()

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
        text_list1 = ['门店', '收银人员', '商品', '会员权益', '活动管理', '券中心', '签约管理', '广告']

        for each in text_list1:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        util.swipe_to_up(self.driver)

        text_list2 = ['客服热线', '帮助中心']

        for each in text_list2:
            self.assertTrue(util.is_textview_exist_by_xpath(self.driver, each))

        util.swipe_to_down(self.driver)

    def test_Mine_Members_rights_vipCard(self):
        # 打开我的tab页面
        util.find_textview_by_xpath_and_click(self.driver, '我的')

        util.find_textview_by_xpath_and_click(self.driver, '会员权益')

        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员日']"))

        util.find_textview_by_xpath_and_click(self.driver, '编辑')

        els2 = self.driver.find_elements_by_xpath("//android.widget.EditText[@index='2']")
        els2[0].clear()
        els2[0].send_keys("qingyu")
        els2[1].clear()
        els2[1].send_keys("vip")

        util.find_textview_by_xpath_and_click(self.driver, '保存')

        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员权益']"))

        self.driver.back()

    def test_Mine_Members_rights_vipDay(self):

        util.find_textview_by_xpath_and_click(self.driver, '我的')

        util.find_textview_by_xpath_and_click(self.driver, '会员权益')

        # 打开我的tab页面
        util.find_textview_by_xpath_and_click(self.driver, '会员日')

        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员日']"))

        # 暂停或开启活动
        # if self.driver.find_element_by_xpath("//android.widget.TextView[@text='进行中']"):
        if util.is_textview_exist_by_xpath(self.driver, '进行中'):
            util.find_textview_by_xpath_and_click(self.driver, '暂停发布')

            el1 = self.driver.find_element_by_id("android:id/button1")
            el1.click()

            WebDriverWait(self, 30).until(lambda x:
                                          self.driver.find_element_by_xpath("//android.widget.TextView[@text='已暂停']"))

        # elif self.driver.find_element_by_xpath("//android.widget.TextView[@text='已暂停']"):
        elif util.is_textview_exist_by_xpath(self.driver, '已暂停'):
            util.find_textview_by_xpath_and_click(self.driver, '重新开启')

            el2 = self.driver.find_element_by_id("android:id/button1")
            el2.click()

            WebDriverWait(self, 30).until(lambda x:
                                          self.driver.find_element_by_xpath("//android.widget.TextView[@text='进行中']"))
        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='重新编辑']"))
        # 重新编辑活动
        util.find_textview_by_xpath_and_click(self.driver, '重新编辑')
        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='编辑会员日']"))

        util.find_textview_by_xpath_and_click(self.driver, '保存')

        WebDriverWait(self, 30).until(lambda x:
                                      self.driver.find_element_by_xpath("//android.widget.TextView[@text='权益详情']"))

        self.driver.back()
        self.driver.back()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(MerchantActivateAndLogin)

    suite = unittest.TestSuite()

    suite.addTest(MerchantActivateAndLogin("test_01_close"))

    # 首页测试
    suite.addTest(MerchantActivateAndLogin("test_find_element_today"))
    suite.addTest(MerchantActivateAndLogin("test_find_element_today_report"))
    #
    # # 会员页测试
    # suite.addTest(MerchantActivateAndLogin("test_find_element_vip"))
    # suite.addTest(MerchantActivateAndLogin("test_find_element_vip_vipList"))
    # suite.addTest(MerchantActivateAndLogin("test_find_element_vip_marketing"))
    #
    # # 消息页面
    # suite.addTest(MerchantActivateAndLogin("test_find_element_Message"))
    #
    # # 我的页面
    # suite.addTest(MerchantActivateAndLogin("test_find_element_Mine"))
    # suite.addTest(MerchantActivateAndLogin("test_Mine_Members_rights_vipCard"))
    # suite.addTest(MerchantActivateAndLogin("test_Mine_Members_rights_vipDay"))

    unittest.TextTestRunner(verbosity=2).run(suite)

