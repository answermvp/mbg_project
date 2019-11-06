import unittest
import time
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.csadmin_page import Csadmin_Page
from poium import Page, PageElement, PageSelect


@ddt
class Check_Ib_Test(unittest.TestCase):
    """
    审核IB注册信息
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
        # au2
        cls.page.get('https://awstau-csadmin.aetos.me')

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

    def test1_signinIB_check(self):
        """审核IB注册信息"""
        # 登录
        self.login_csadmin('admin', 'aa1111')
        # 点击待审核IB资料
        time.sleep(1)
        self.page.check_IB.click()
        # 点击审核地址证明
        time.sleep(2)
        self.page.cleck_addre.click()
        # 点击复审通过按钮
        self.page.IB_review2suss_button.click()
        time.sleep(5)
        # 点击审核身份证明
        time.sleep(1)
        self.page.check_identity.click()
        # 点击复审通过按钮
        self.page.IB_review2suss_button.click()
        time.sleep(5)
        # 点击用户列表
        self.page.user_list.click()
        # 点击用户列表的查询按钮
        time.sleep(2)
        self.page.userlist_submit.click()
        # 点击用户列表中第一行的IB用户名
        time.sleep(2)
        self.page.IB_name.click()
        # 点击IB信息
        self.page.IB_info.click()
        time.sleep(2)
        # 选择IB状态
        time.sleep(2)
        PageSelect(self.page.IB_state, value='5')
        # 选择累计入金限额
        time.sleep(2)
        PageSelect(self.page.IB_amountLimit, value='10000.00')
        # 点击保存IB信息
        self.page.IB_info_save.click()
        time.sleep(2)
        self.page.accept_alert()
        time.sleep(8)
        # 点击用户列表
        self.page.user_list.click()
        # 点击用户列表的查询按钮
        time.sleep(3)
        self.page.userlist_submit.click()
        # 点击是否新客户
        self.page.IB_newuser_div.click()
        time.sleep(2)
        # 点击资料
        self.page.info.click()
        time.sleep(5)
        # 点击开启IB账号
        self.page.approved.click()
        time.sleep(2)
        # 确认开启
        self.page.affirm_button.click()
        time.sleep(10)
        # 点击用户列表
        self.page.user_list.click()
        # 点击用户列表的查询按钮
        time.sleep(2)
        self.page.userlist_submit.click()
        # 点击第3行的是否新客户
        time.sleep(2)
        self.page.IB_line3_div.click()
        # 点击IB的入
        time.sleep(2)
        self.page.IB_in.click()
        # 输入入金金额
        self.page.Ib_in_money.send_keys('1000')
        # 输入入金 comment
        self.page.Ib_in_comment.send_keys('test')
        # 输入入金说明
        self.page.Ib_in_remarks.send_keys('测试')
        # 提交入金
        time.sleep(2)
        self.page.Ib_in_submit.click()
        # 确认入金信息
        self.page.Ib_in_accept.click()
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
