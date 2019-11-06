import unittest
import time
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.csadmin_page import Csadmin_Page
from selenium.webdriver.common.action_chains import ActionChains
from poium import Page, PageElement, PageSelect


@ddt
class Check_Test(unittest.TestCase):
    """
    csadmin 审核 live 客户
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
        cls.page = Csadmin_Page(cls.dr)
        # MBG
        cls.page.get('http://csadmin.mbgmarkets.me')

    def setUp(self):
        pass

    def login_csadmin(self, username, password):
        """登录"""
        # 输入用户名
        self.page.username_input.clear()
        self.page.username_input.send_keys(username)
        # 输入密码
        self.page.password_input.clear()
        self.page.password_input.send_keys(password)
        # 点击登录按钮
        self.page.submit_button.click()

    def test1_signin_check(self):
        """审核live客户注册信息"""
        # 登录
        self.login_csadmin('admin', 'aa1111')
        # 点击待审核银行信息
        # self.page.bank_info.click()
        # # 点击审核
        # self.page.bankinfo_check_button.click()
        # # 点击复审通过按钮
        # self.page.review2suss_button.click()
        # time.sleep(5)
        # 点击待审客户资料
        self.page.clt_info.click()
        # 点击第一行审核
        self.page.clt_check_1.click()
        # 点击复审通过按钮
        self.page.clt_review2suss_button.click()
        time.sleep(5)
        # 点击第二行审核
        self.page.clt_check_2.click()
        # 点击复审通过按钮
        self.page.clt_review2suss_button.click()
        time.sleep(5)
        # 点击用户列表
        self.page.user_list.click()
        # 点击用户列表的查询按钮
        time.sleep(2)
        self.page.userlist_submit.click()
        # 点击用户列表中第一行的用户名
        time.sleep(2)
        self.page.username.click()
        # 点击交易账号
        time.sleep(2)
        self.page.transaction_num.click()
        # 选择客户状态
        time.sleep(2)
        PageSelect(self.page.user_state_select, value='5')
        # 提交客户状态
        time.sleep(2)
        self.page.userstate_submit.click()
        self.page.accept_alert()
        time.sleep(5)
        # 点击用户列表中第一行的用户名
        self.page.username.click()
        # 点击交易账号
        time.sleep(2)
        self.page.transaction_num.click()
        # 选择累计入金限额
        time.sleep(2)
        PageSelect(self.page.quota_select, value='500.00')
        # 提交入金限额修改
        self.page.quota_submit.click()
        time.sleep(2)
        self.page.accept_alert()
        time.sleep(5)
        # 点击用户列表
        self.page.user_list.click()
        # 点击用户列表的查询按钮
        time.sleep(2)
        self.page.userlist_submit.click()
        # 点击用户的 DP
        time.sleep(2)
        self.page.dp_button.click()
        # 输入入金金额
        self.page.in_num.send_keys('0')
        # 输入入金 comment
        self.page.comment.send_keys('test')
        # 输入入金说明
        self.page.remarks.send_keys('测试')
        # 提交入金
        time.sleep(2)
        self.page.in_submit.click()
        # 确认入金信息
        self.page.in_accept.click()
        time.sleep(5)



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

