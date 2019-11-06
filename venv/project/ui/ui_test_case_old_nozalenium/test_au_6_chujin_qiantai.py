import unittest
import time
import datetime
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.chujin_page import Chujin_Page
from selenium.webdriver.common.action_chains import ActionChains
from poium import Page, PageElement, PageSelect
from testdata.read_excel import get_testdata
from testdata.mysql_client import mysql_client


# 指定 excel 文件路径
excel_file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '//' + 'testdata' + '//' + 'signin_testdata_new.xlsx'

# 获取列表中的数据
# 1，2 = 获取第1行（从1开始算，不包括第2行）；0， 4 = 获取前4列（从0开始算，不包括第4列）
signinib_1_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 2, 0, 4)
# 获取第1行4到19列
signinib_2_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 2, 4, 19)
# 获取第1行19到21列
signinib_3_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 2, 21, 23)

@ddt
class Chujin_test(unittest.TestCase):
    """
    测试 au2 前台出金
    使用数据库的方式
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
        cls.page = Chujin_Page(cls.dr)
        # au2 前台登录链接
        cls.page.get('https://awstau-trust.aetos.me/cn/login.htm')
        # 时间戳，用于注册用户名拼接
        cls.time_now = str(datetime.datetime.now().strftime('%m%d%H%M'))
        # 获取操作数据库的对象
        cls.mysql = mysql_client()
        # 查询数据库中最新注册的用户名
        cls.username = cls.mysql.get_data("SELECT email FROM t_user_account ORDER BY userId DESC limit 1;")[0][0]

    def setUp(self):
        pass

    def login(self, username, password):
        """登录"""
        # 输入电邮
        self.page.username_input.clear()
        self.page.username_input.send_keys(username)
        # 输入密码
        self.page.password_input.clear()
        self.page.password_input.send_keys(password)
        # 点击登录按钮
        self.page.login_button.click()

    def test_chujin(self):
        """前台出金"""
        self.login(self.username, '123456789aA')
        # 点击出入金管理
        self.page.churujinguanli_a.click()
        # 点击出金
        self.page.chujin_span.click()
        # 获取当前句柄
        now_handle = self.dr.current_window_handle
        # 获取所有句柄
        all_handle = self.dr.window_handles
        # 遍历所有句柄
        for handle in all_handle:
            if handle != now_handle:
                new_handle = handle
                # 切换到新的标签页
                self.dr.switch_to_window(new_handle)
        # 输入出金金额
        self.page.chujin_num_input.send_keys(50)
        # 输入登录密码
        self.page.login_password_input.clear()
        self.page.login_password_input.send_keys('123456789aA')
        # 点击提交按钮
        self.page.submin_button.click()
        # 点击确认按钮
        self.page.affirm_button.click()
        # 确认提交
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