# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait


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

    @classmethod
    def tearDownClass(cls):
        # super(MerchantActivateAndLogin, cls).tearDownClass()
        cls.driver.quit()

    def test_merchant_activate(self):
        self.driver.implicitly_wait(2)

        el1 = self.driver.find_element_by_id("android:id/button1")
        el1.click()

        el2 = self.driver.find_element_by_xpath("//android.widget.EditText[@text='输入手机号/商户号']")
        el2.send_keys("A00303780000001")
        el3 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='激活']")
        el3.click()

        el4 = self.driver.find_element_by_id("android:id/button1")
        el4.click()

    def test_merchant_login(self):
        self.driver.implicitly_wait(2)

        # 商户登录
        el5 = self.driver.find_element_by_accessibility_id("login_user_code")
        el5.send_keys("A00303780000001")
        el6 = self.driver.find_element_by_accessibility_id("login_pwd_code")
        el6.send_keys("a123456")
        self.driver.hide_keyboard()

        els3 = self.driver.find_elements_by_xpath("//android.widget.TextView[@text='登录']")
        els3[0].click()

        # 关闭引导弹框
        els3 = self.driver.find_elements_by_xpath("//android.widget.TextView[@text='我知道了']")
        els3[0].click()

    def test_merchant_today(self):

        # 商户登录成功之后，首页的页面元素
        text_list = ['今日交易额（账本）', '去收款', '充值金额', '新增会员', '查看盈亏', '会员招募', '群体发券', '充值送礼', '累充送礼',
                    '今日', '会员', '消息', '我的']

        try:
            for each in text_list:
                locator = "//android.widget.TextView[@text=\'" + each + "\']"
                print(locator)
                WebDriverWait(self, 3).until(lambda x: self.driver.find_element_by_xpath(locator))
                self.assertIsNotNone(self.driver.find_element_by_xpath(locator))

        finally:
            print('test_merchant_today')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MerchantActivateAndLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
