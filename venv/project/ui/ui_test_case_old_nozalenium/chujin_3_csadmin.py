import unittest
import time
import datetime
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.csadmin_page import Csadmin_Page
from selenium.webdriver.common.action_chains import ActionChains
from poium import Page, PageElement, PageSelect
from testdata.read_excel import get_testdata
from testdata.mysql_client import mysql_client
from selenium.webdriver.common.keys import Keys


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
    测试 au2 后台出金
    """
    @classmethod
    def setUpClass(cls):
        """初始化"""
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()        
        cls.page = Csadmin_Page(cls.dr)
        # 后台 csadmin 登录链接
        cls.page.get('https://awstau-csadmin.aetos.me/index.php/Public/login')
        # 时间戳，用于注册用户名拼接
        #cls.time_now = str(datetime.datetime.now().strftime('%m%d%H%M'))
        # 获取操作数据库的对象
        cls.mysql = mysql_client()
        # 查询数据库中最新注册的用户名
        cls.username = cls.mysql.get_data("SELECT email FROM t_user_account ORDER BY userId DESC limit 1;")[0][0]

    def setUp(self):
        pass

    def login_csadmin(self, username, password):
        """登录 csadmin """
        # 输入用户名
        time.sleep(5)
        self.page.username_input.clear()
        self.page.username_input.send_keys(username)
        # 输入密码
        self.page.password_input.clear()
        self.page.password_input.send_keys(password)
        # 点击登录按钮
        self.page.submit_button.click()

    def test_step1(self):
        """
        出金流程第一步
        Cs Check
        """
        self.login_csadmin('cs_test', 'aa1111')
        # 点击出金管理
        time.sleep(5)
        self.page.chujinguanli_span.click()
        # 点击 CS Check
        time.sleep(3)
        self.page.cs_check_a.click()
        # 在 cs check 的 username 搜索框输入用户名
        time.sleep(3)
        self.page.cs_check_username_input.send_keys(self.username)
        # 点击 submit 按钮
        time.sleep(5)
        self.page.cs_check_username_submit.click()
        # checkstatus 选择 confirmed
        time.sleep(3)
        PageSelect(self.page.cs_check_checkstatus_select, value='2')
        # 在 comment 输入 test
        time.sleep(3)
        self.page.cs_check_comment_input.send_keys('test')
        # 点击 submit
        time.sleep(2)
        self.page.cs_check_action_submit.click()
        time.sleep(2)
        # 确认提交
        self.page.accept_alert()
        # 点击退出
        time.sleep(5)
        self.page.log_out.click()

    def test_step2(self):
        """
        出金流程第二步
        Risk Check
        """
        self.login_csadmin('risk_test', 'aa1111')
        # 点击出金管理
        time.sleep(5)
        self.page.chujinguanli_span.click()
        # 点击 risk check
        time.sleep(3)
        self.page.risk_check_a.click()
        # 在搜索框输入用户名
        time.sleep(2)
        self.page.risk_check_username_input.send_keys(self.username)
        # 点击 submit 按钮
        time.sleep(3)
        self.page.risk_check_username_submit.click()
        # checkstatus 选择 confirmed
        time.sleep(3)
        PageSelect(self.page.risk_check_checkstatus_select, value='2')
        # 在 comment 输入 test
        time.sleep(3)
        self.page.risk_check_comment_input.send_keys('test')
        # 点击 submit
        time.sleep(2)
        self.page.risk_check_action_submit.click()
        time.sleep(2)
        # 确认提交
        self.page.accept_alert()
        # 点击退出
        time.sleep(5)
        self.page.log_out.click()

    def test_step3_1(self):
        """
        出金流程第三步
        Settlement Check
        （1）WD Standing Setup
        """
        self.login_csadmin('stm_test', 'aa1111')
        # 点击出金管理
        time.sleep(5)
        self.page.chujinguanli_span.click()
        # 点击 WD Standing Setup
        time.sleep(3)
        self.page.wd_standing_setup_a.click()
        # 在搜索框输入用户名
        time.sleep(2)
        self.page.wd_standing_setup_username_input.send_keys(self.username)
        # 点击 submint
        time.sleep(2)
        self.page.wd_standing_setup_username_submit.click()
        # 勾选搜索出来的数据
        time.sleep(3)
        self.page.wd_standing_setup_checkbox.click()
        # 点击 process
        time.sleep(3)
        self.page.wd_standing_setup_process.click()
        # 确认
        time.sleep(1)
        self.page.wd_standing_setup_alert.click()
        # 点击退出
        time.sleep(3)
        self.page.log_out.click()

    def test_step3_2(self):
        """
        出金流程第三步
        Settlement Check
        （2）WD Allocation
        """
        self.login_csadmin('stm_test', 'aa1111')
        # 点击出金管理
        time.sleep(5)
        self.page.chujinguanli_span.click()
        # 点击 wd alloction
        time.sleep(5)
        self.page.wd_alloction_a.click()
        # 在搜索框输入用户名
        time.sleep(3)
        self.page.wd_alloction_username_input.send_keys(self.username)
        # 点击 submit
        time.sleep(3)
        self.page.wd_alloction_username_submit.click()
        # 选中搜索到的数据
        time.sleep(3)
        self.page.wd_alloction_item_div.click()
        # 点击 allocate
        time.sleep(2)
        self.page.wd_alloction_allocate_span.click()
        # 输入金额
        time.sleep(5)
        self.page.wd_allocions_allocate_anount_input.click()
        time.sleep(2)
        self.page.wd_allocions_allocate_anount_input.send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        self.page.wd_allocions_allocate_anount_input.send_keys(50)
        # # 输入 fee
        # time.sleep(5)
        # self.page.wd_allocions_fee_input.click()
        # self.page.wd_allocions_fee_input.clear()
        # self.page.wd_allocions_fee_input.send_keys(0)
        # 点击 allocate 按钮
        time.sleep(2)
        self.page.wd_allocions_allocate_button.click()
        # 点击退出按钮
        time.sleep(3)
        self.page.log_out.click()

    def test_step4_1(self):
        """
        出金流程第四步
        Operation Check
        (1) WD Alloc Review
        """
        self.login_csadmin('opr_test', 'aa1111')
        # 点击出金管理
        time.sleep(5)
        self.page.chujinguanli_span.click()
        # 点击 WD Alloc Review
        time.sleep(3)
        self.page.wd_alloc_review_a.click()
        # 在搜索框输入用户名
        time.sleep(3)
        self.page.wd_alloc_review_username_input.send_keys(self.username)
        # 点击 submit
        time.sleep(3)
        self.page.wd_alloc_review_username_submit.click()
        # 点击 review
        time.sleep(3)
        self.page.wd_alloc_review_review_a.click()
        # 点击 confirm
        time.sleep(3)
        self.page.wd_alloc_review_confirm_button.click()
        # 点击退出按钮
        time.sleep(3)
        self.page.log_out.click()

    def test_step4_2(self):
        """
        出金流程第四步
        Operation Check
        (2) Instruction Prepare
        """
        self.login_csadmin('stm_test', 'aa1111')
        # 点击出金管理
        time.sleep(5)
        self.page.chujinguanli_span.click()



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