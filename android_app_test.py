# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait


def swipe_to_left(driver, duration=None):
    try:
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')

        driver.swipe(width/6*5, height/2, width/6, height/2, duration)

    except Exception as ex:
        print(ex)


def find_textview_by_xpath_and_click(driver, name):
    els = driver.find_element_by_xpath("//android.widget.TextView[@text=\'" + name + "\']")
    if isinstance(els, list):
        els[0].click()
    else:
        els.click()


class MerchantActivateAndLogin(unittest.TestCase):
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
        cls.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        # super(MerchantActivateAndLogin, cls).tearDownClass()
        cls.driver.quit()

    def test_merchant_activate(self):
        # self.driver.implicitly_wait(2)

        el1 = self.driver.find_element_by_id("android:id/button1")
        el1.click()

        # 引导页，左滑动屏幕
        swipe_to_left(self.driver)
        swipe_to_left(self.driver)
        swipe_to_left(self.driver)

        # el2 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='立即体验']")
        # el2.click()

        find_textview_by_xpath_and_click(self.driver, '立即体验')

        el3 = self.driver.find_element_by_xpath("//android.widget.EditText[@text='输入手机号/商户号']")
        el3.send_keys("A00303780000001")

        find_textview_by_xpath_and_click(self.driver, '激活')
        # el4 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='激活']")
        # el4.click()

        el5 = self.driver.find_element_by_id("android:id/button1")
        el5.click()

    def test_merchant_login(self):
        # self.driver.implicitly_wait(2)

        # 商户登录
        el5 = self.driver.find_element_by_accessibility_id("login_user_code")
        el5.send_keys("A00303780000001")
        el6 = self.driver.find_element_by_accessibility_id("login_pwd_code")
        el6.send_keys("a123456")
        self.driver.hide_keyboard()

        find_textview_by_xpath_and_click(self.driver, '登录')
        # els3 = self.driver.find_elements_by_xpath("//android.widget.TextView[@text='登录']")
        # els3[0].click()

        # 关闭引导弹框
        # els3 = self.driver.find_elements_by_xpath("//android.widget.TextView[@text='我知道了']")
        # els3[0].click()
        find_textview_by_xpath_and_click(self.driver, '我知道了')

    def test_find_element_today(self):

        # 商户登录成功之后，首页的页面元素
        text_list = ['今日交易额（账本）', '去收款', '充值金额', '新增会员', '查看盈亏', '会员招募', '群体发券', '充值送礼', '累充送礼',
                     '今日', '会员', '消息', '我的']

        try:
            for each in text_list:
                locator = "//android.widget.TextView[@text=\'" + each + "\']"
                els = self.driver.find_element_by_xpath(locator)
                WebDriverWait(self, 3).until(lambda x: els)
                self.assertIsNotNone(els)

        except Exception as ex:
            print(ex)

    def test_find_element_today_report(self):
        find_textview_by_xpath_and_click(self.driver, '查看盈亏')
        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='日交易报表']"))

    def test_find_element_vip(self):

        self.driver.back()

        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员']"))

        # 打开会员tab页面
        find_textview_by_xpath_and_click(self.driver, '会员')

        # 会员页的页面元素
        text_list = ['会员', '总会员', '价值', '普通', '沉睡', '流失', '上周数据',
                     '会员新增', '复购率', '流失率', '会员消费占比', '会员平均客单价', '查看完整数据周报',
                     '招募会员', '增加黏性', '流失挽回']

        try:
            for each in text_list:
                locator = "//android.widget.TextView[@text=\'" + each + "\']"
                els = self.driver.find_element_by_xpath(locator)
                WebDriverWait(self, 3).until(lambda x: els)
                self.assertIsNotNone(els)

        except Exception as ex:
            print(ex)

    # def test_find_element_vip_vipList(self):
    #     # 打开会员列表页面
    #     els1 = self.driver.find_elements_by_xpath("//android.widget.ImageView[@index='0']")
    #     els1[0].click()
    #
    #     self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员列表']"))

    def test_find_element_vip_marketing(self):
        # self.driver.back()

        WebDriverWait(self, 10).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='招募会员']"))

        # els1 = self.driver.find_elements_by_xpath("//android.widget.TextView[@text='招募会员']")
        # els1[0].click()
        find_textview_by_xpath_and_click(self.driver, '招募会员')

        # 会员招募
        WebDriverWait(self, 10).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='招募方式']"))

        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='开卡送券']"))

        # 增加黏性
        swipe_to_left(self.driver)
        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='充值有礼']"))
        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='累充送礼']"))

        # 流失挽回
        swipe_to_left(self.driver)
        self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='群体发券']"))

    def test_find_element_Message(self):
        self.driver.back()

        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='消息']"))

        # 打开消息tab页面
        # els1 = self.driver.find_elements_by_xpath("//android.widget.TextView[@text='消息']")
        # els1[0].click()
        find_textview_by_xpath_and_click(self.driver, '消息')

        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='消息中心']"))

        if self.driver.find_element_by_xpath("//android.widget.TextView[@text='平台活动']"):
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='最新平台活动资讯']"))

        elif self.driver.find_element_by_xpath("//android.widget.TextView[@text='公告']"):
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='官方公告']"))

        elif self.driver.find_element_by_xpath("//android.widget.TextView[@text='系统通知']"):
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='系统反馈信息']"))

        # elif self.driver.find_element_by_xpath("//android.widget.TextView[@text='数据报表']"):
        #     self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='定期的运营数据推送']"))
        else:
            self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='您还没有新的消息']"))

    def test_find_element_Mine(self):

        # 打开我的tab页面
        # els1 = self.driver.find_elements_by_xpath("//android.widget.TextView[@text='我的']")
        # els1[0].click()
        find_textview_by_xpath_and_click(self.driver, '我的')

        # 会员页的页面元素
        text_list = ['商户号', '门店', '收银人员', '商品', '会员权益', '活动管理', '券中心', '签约管理',
                     '广告', '客服热线', '帮助中心']

        try:
            for each in text_list:
                locator = "//android.widget.TextView[@text=\'" + each + "\']"
                els = self.driver.find_element_by_xpath(locator)
                WebDriverWait(self, 3).until(lambda x: els)
                self.assertIsNotNone(els)

        except Exception as ex:
            print(ex)

    def test_Mine_Members_rights_vipCard(self):
        # 打开我的tab页面
        find_textview_by_xpath_and_click(self.driver, '会员权益')

        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员日']"))

        find_textview_by_xpath_and_click(self.driver, '编辑')

        els2 = self.driver.find_elements_by_xpath("//android.widget.EditText[@index='2']")
        els2[0].clear()
        els2[0].send_keys("qingyu")
        els2[1].clear()
        els2[1].send_keys("vip")

        find_textview_by_xpath_and_click(self.driver, '保存')

        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员权益']"))

    def test_Mine_Members_rights_vipDay(self):
        # 打开我的tab页面
        find_textview_by_xpath_and_click(self.driver, '会员日')

        WebDriverWait(self, 10).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='会员日']"))

        # 暂停或开启活动
        # if self.driver.find_element_by_xpath("//android.widget.TextView[@text='进行中']"):
        #     find_textview_by_xpath_and_click(self.driver, '暂停发布')
        #
        #     el1 = self.driver.find_element_by_id("android:id/button1")
        #     el1.click()
        #
        #     WebDriverWait(self, 5).until(lambda x:
        #                                  self.driver.find_element_by_xpath("//android.widget.TextView[@text='已暂停']"))
        #
        # elif self.driver.find_element_by_xpath("//android.widget.TextView[@text='已暂停']"):
        #     find_textview_by_xpath_and_click(self.driver, '重新开启')
        #
        #     el2 = self.driver.find_element_by_id("android:id/button1")
        #     el2.click()
        #
        #     WebDriverWait(self, 5).until(lambda x:
        #                                  self.driver.find_element_by_xpath("//android.widget.TextView[@text='进行中']"))
        # 重新编辑活动
        find_textview_by_xpath_and_click(self.driver, '重新编辑')
        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='编辑会员日']"))
        find_textview_by_xpath_and_click(self.driver, '保存')
        WebDriverWait(self, 5).until(lambda x:
                                     self.driver.find_element_by_xpath("//android.widget.TextView[@text='权益详情']"))


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(MerchantActivateAndLogin)

    suite = unittest.TestSuite()

    # 商户登录
    suite.addTest(MerchantActivateAndLogin("test_merchant_activate"))
    suite.addTest(MerchantActivateAndLogin("test_merchant_login"))

    # 首页测试
    suite.addTest(MerchantActivateAndLogin("test_find_element_today"))
    suite.addTest(MerchantActivateAndLogin("test_find_element_today_report"))

    # 会员页测试
    suite.addTest(MerchantActivateAndLogin("test_find_element_vip"))
    # suite.addTest(MerchantActivateAndLogin("test_find_element_vip_vipList"))
    suite.addTest(MerchantActivateAndLogin("test_find_element_vip_marketing"))

    # 消息页面
    suite.addTest(MerchantActivateAndLogin("test_find_element_Message"))

    # 我的页面
    suite.addTest(MerchantActivateAndLogin("test_find_element_Mine"))
    suite.addTest(MerchantActivateAndLogin("test_Mine_Members_rights_vipCard"))
    suite.addTest(MerchantActivateAndLogin("test_Mine_Members_rights_vipDay"))

    unittest.TextTestRunner(verbosity=2).run(suite)

