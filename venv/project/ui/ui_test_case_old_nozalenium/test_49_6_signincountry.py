import unittest
import time
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.signinuser_page import IBSignIn_Page
from selenium.webdriver.common.action_chains import ActionChains
from poium import Page, PageElement, PageSelect
from testdata.read_excel import get_testdata


# 指定 excel 文件路径
excel_file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '//' + 'testdata' + '//' + 'signin_countrydata.xlsx'
# 获取列表中的数据
# 1，2 = 获取第1行（从1开始算，不包括第2行）；0， 4 = 获取前4列（从0开始算，不包括第4列）
# all
country_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 250, 0, 2)
# 第4行
# country_testdata = get_testdata(excel_file_dir, 'Sheet1', 4, 5, 0, 2)
# 第5行
# country_testdata = get_testdata(excel_file_dir, 'Sheet1', 5, 6, 0, 2)
# 第1行到第3行
# country_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 4, 0, 2)



@ddt
class Signin_Country_test(unittest.TestCase):
    """
    测试注册不同的国家
    """
    @classmethod
    def setUpClass(cls):
        """初始化"""
        # cls.dr = webdriver.Chrome()
        # <--------------------------------后加的
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        # 隐藏 GUI
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        cls.dr = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options) 
        # 后加的--------------------------------- >
        cls.dr.maximize_window()        
        cls.page = IBSignIn_Page(cls.dr)
        # IB 开户链接注册
        cls.page.get('https://awstau-trust.aetos.me/12013130-C05')

    def setUp(self):
        pass

    @data(*country_testdata)
    @unpack
    def test_signi_country_1(self, country_value, expect_error_info):
        """测试国家"""
        # 选择国家
        PageSelect(self.page.country_select, value=country_value)
        # 勾选我同意打开错误弹窗
        time.sleep(2)
        self.page.agreement1_checkbox.click()
        try:
            # 点击取消弹窗
            time.sleep(1)
            self.page.country_error_button.click()
        except:
            print ('无弹窗')
        error_info = self.page.error_info.text
        actual_error_info = error_info.split('，', 1)[0]
        self.assertEqual(actual_error_info, expect_error_info.split('，', 1)[0])
        time.sleep(1)
        self.page.refresh_element(self.page)
        time.sleep(1)

    def tearDown(self):
        pass
      
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        time.sleep(5)
        cls.dr.quit()

if __name__ == '__main__':
    unittest.main()