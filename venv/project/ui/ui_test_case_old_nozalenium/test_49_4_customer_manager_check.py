import unittest
import time
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.customer_manager_check_page import Customer_Manager_Check_Page   
from poium import Page, PageElement, PageSelect


@ddt
class Customer_Manager_Check__Test(unittest.TestCase):
    """
    客户经理给IB划分等级
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
        cls.page = Customer_Manager_Check_Page(cls.dr)
        # 4.2
        cls.page.get('https://awstau-trust.aetos.me')
        # 4.9 MBG
        cls.page.get('https://awst49-trust.aetos.me')

    def setUp(self):
        pass

    def login(self, username, password):
        """客户经理登录"""
        # 输入用户名
        self.page.username_input.clear()
        self.page.username_input.send_keys(username)
        # 输入密码
        self.page.password_input.clear()
        self.page.password_input.send_keys(password)
        # 点击登录按钮
        self.page.login_button.click()

    def test1_customer_manager_check(self):
        """客户经理给IB指定等级"""
        # 登录
        self.login('aetosdemoam2', '123456789aA')
        # 点击客户管理
        self.page.Client_mgmt_a.click()
        # 点击意向IB
        self.page.intention_IB.click()
        # 点击待跟进IB
        self.page.follow_up_IB.click()
        # 点击IB用户名
        self.page.IB_username.click()
        # 进入IB信息表单
        self.page.switch_to_frame(self.page.IB_info_iframe)
        # 选择IB等级--选择标准
        PageSelect(self.page.IB_grade_select, value='100')
        # 点击保存按钮
        self.page.save_button.click()
        # 退出IB信息表单
        # self.page.switch_to_frame_out()
        time.sleep(2)
        # 点击确定
        self.page.accept_alert()
        time.sleep(1)
        # 点击确定
        self.page.accept_alert()




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
