import unittest
import datetime, time
from selenium import webdriver
from ddt import ddt, file_data, data, unpack
from poium import Page, PageElement, PageSelect
from pages.signinuser_page import UserSignIn_Page


@ddt
class SigninUser_error(unittest.TestCase):
    """注册功能异常测试用例"""
    @classmethod
    def setUpClass(cls):
        """初始化"""
        # cls.dr = webdriver.Chrome()
        # <--------------------------------后加的
        options = webdriver.ChromeOptions()
        # 禁用 chrome 扩展
        options.add_argument('--disable-extensions')
        # 隐藏 GUI
        # options.add_argument('--headless')
        # 禁用 chrome GPU 硬件加速
        options.add_argument('--disable-gpu')
        # 让 chrome 以 root 权限运行
        options.add_argument('--no-sandbox')
        cls.dr = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options) 
        # 后加的--------------------------------- >
        cls.dr.maximize_window()
        cls.page = UserSignIn_Page(cls.dr)
        # MBG 注册 demo 用户
        cls.page.get('https://trust.mbgmarkets.me/cn/register-demo.htm')
        # 时间戳，用于注册用户名拼接
        cls.time_now = str(datetime.datetime.now().strftime('%y%m%d%H%M'))
        # 正确的用户名
        cls.true_username = 'test_answer_' + cls.time_now + '@email.com'


    def setUp(self):
        pass

    @data(
        [' ', '请输入真实有效的电邮'],
        ['@', '请输入真实有效的电邮'],
        [111111, '请输入真实有效的电邮']
    )
    @unpack
    def test_01_emaill_error(self, input, error_message):
        """email error"""
        self.page.email_input.click()
        self.page.email_input.clear()
        self.page.email_input.send_keys(input)
        time.sleep(1)
        self.page.password_input.click()
        self.assertEqual(self.page.email_message.text, error_message)

    # @data(
    #     ['','请输入10-15个字符，含且仅含英文大写字母、小写字母和数字'],
    #     [111,'请输入10-15个字符，含且仅含英文大写字母、小写字母和数字'],
    #     [12345678910,'请输入10-15个字符，含且仅含英文大写字母、小写字母和数字'],
    # )
    # @unpack
    # def test_02_password_error(self, password1, password1_error_message):
    #     """password error"""
    #     self.page.password_input.click()
    #     self.page.password_input.clear()
    #     self.page.password_input.send_keys(password1)
    #     self.page.password2_input.click()
    #     self.assertEqual(self.page.password1_message.text, password1_error_message)

    # @data(
    #     ['123456789aA', ' ', '两次输入的密码不一致，请重新输入']
    # )
    # @unpack
    # def test_03_password2_error(self, password1, password2, password2_error_message):
    #     """password2 error"""
    #     self.page.password_input.click()
    #     self.page.password_input.send_keys(password1)
    #     self.page.password2_input.click()
    #     self.page.password2_input.send_keys(password2)
    #     self.page.phone_input.click()
    #     self.assertEqual(self.page.password2_message.text, password2_error_message)

    # @data(
    #     [' '],
    #     [00000000000],
    #     ['测试']
    # )
    # @unpack
    # def test_04_phonenumber_error(self, phone):
    #     """phonenumber error"""
    #     phone_error_message_list = ['请输入手机号码', '请输入完整正确手机号码']
    #     self.page.phone_input.click()
    #     self.page.phone_input.clear()
    #     self.page.phone_input.send_keys(phone)
    #     self.assertIn(self.page.phone_message.text, phone_error_message_list)

    # @file_data('/root/venv/project/ui/testdata/country_new.json')
    # def test_05_country_error(self, country):
    #     """country error"""
    #     PageSelect(self.page.country_select, value=country)
    #     self.page.phone_input.click()
    #     if country == 'US':
    #         country_error_message = '目前MBG Markets无法服务您所在的国家或地区'
    #         couny_right_message = self.page.country_right.text
    #         self.assertEqual(couny_right_message, country_error_message)

    def register(self, email, password, password2, phone):
        """register"""
        # 输入电邮
        time.sleep(2)
        self.page.email_input.clear()
        self.page.email_input.send_keys(email)
        # 输入密码
        time.sleep(2)
        self.page.password_input.clear()
        self.page.password_input.send_keys(password)
        # 确认密码
        time.sleep(2)
        self.page.password2_input.clear()
        self.page.password2_input.send_keys(password2)
        # 输入手机号码
        time.sleep(2)
        self.page.phone_input.clear()
        self.page.phone_input.send_keys(phone)
        # 选择国家
        PageSelect(self.page.country_select, value='CN')
        # 清空交易编码
        # self.page.affiliate_code_input.clear()
        # 已阅读
        self.page.agreement1_checkbox.click()
        # 我同意
        self.page.isOptOut_checkbox.click()
        # 点击注册
        time.sleep(1)
        self.page.signin_button.click()

    # def register_no_select(self, email, password, password2, phone):
    #     """register 两个协议都不勾选"""
    #     # 输入电邮
    #     time.sleep(2)
    #     self.page.email_input.clear()
    #     self.page.email_input.send_keys(email)
    #     # 输入密码
    #     time.sleep(2)
    #     self.page.password_input.clear()
    #     self.page.password_input.send_keys(password)
    #     # 确认密码
    #     time.sleep(2)
    #     self.page.password2_input.clear()
    #     self.page.password2_input.send_keys(password2)
    #     # 输入手机号码
    #     time.sleep(2)
    #     self.page.phone_input.clear()
    #     self.page.phone_input.send_keys(phone)
    #     # 选择国家
    #     PageSelect(self.page.country_select, value='CN')
    #     # 清空交易编码
    #     # self.page.affiliate_code_input.clear()
    #     # # 已阅读
    #     # self.page.agreement1_checkbox.click()
    #     # # 我同意
    #     # self.page.isOptOut_checkbox.click()
    #     # 点击注册
    #     time.sleep(1)
    #     self.page.signin_button.click()
    #     self.page.signin_button.click()

    # def register_select_two(self, email, password, password2, phone):
    #     """register 勾选第2个协议"""
    #     # 输入电邮
    #     time.sleep(2)
    #     self.page.email_input.clear()
    #     self.page.email_input.send_keys(email)
    #     # 输入密码
    #     time.sleep(2)
    #     self.page.password_input.clear()
    #     self.page.password_input.send_keys(password)
    #     # 确认密码
    #     time.sleep(2)
    #     self.page.password2_input.clear()
    #     self.page.password2_input.send_keys(password2)
    #     # 输入手机号码
    #     time.sleep(2)
    #     self.page.phone_input.clear()
    #     self.page.phone_input.send_keys(phone)
    #     # 选择国家
    #     PageSelect(self.page.country_select, value='CN')
    #     # 清空交易编码
    #     # self.page.affiliate_code_input.clear()
    #     # 已阅读
    #     # self.page.agreement123456789aA
    #     # # 我同意
    #     self.page.isOptOut_ch123456789aA
    #     # 点击注册
    #     time.sleep(1)
    #     self.page.signin_butt123456789aA
    #     self.page.signin_butt123456789aA

    # def test_06_agreement_error123456789aA
    #     """agreement error"""123456789aA
    #     self.register_no_select(self.true_username, '123456789aA', '123456789aA', self.time_now)
    #     # self.assertIsNone(self.page.accept_alert())
    #     self_text = self.page.get_alert_text()
    #     text = '请阅读并接受协议'
    #     self.assertEqual( self_text, text)
    #     self.page.accept_alert()

    # def test_07_agreement_error_1(self):
    #     """agreement error"""
    #     self.register_select_two(self.true_username, '123456789aA', '123456789aA', self.time_now)
    #     # self.assertIsNone(self.page.accept_alert())
    #     self_text = self.page.get_alert_text()
    #     text = '请阅读并接受协议'
    #     self.assertEqual( self_text, text)
    #     self.page.accept_alert()

    # def test_08_goto_step2(self):
    #     """goto step2"""
    #     self.register(self.true_username, '123456789aA', '123456789aA', self.time_now)
    #     time.sleep(5)
    #     # 点击完善资料并开立真实账户按钮
    #     self.page.demo_up_info_button.click()

    # @data(
    #     [' ', '请输入您证件上名字的拼音'],
    #     [111, '请输入您证件上名字的拼音'],
    #     ['测试', '请输入您证件上名字的拼音'],
    #     ['test', '请输入您证件上名字的拼音']
    # )
    # @unpack
    # def test_09_surname_error(self, surname, surname_error_message):
    #     """surname error"""
    #     self.page.surName_input.clear()
    #     self.page.surName_input.send_keys(surname)
    #     self.page.lastName_input.click()
    #     self.assertEqual(self.page.surName_right.text, surname_error_message)

    # @data(
    #     [' ', '请输入您证件上姓氏的拼音'],
    #     [111, '请输入您证件上姓氏的拼音'],
    #     ['测试', '请输入您证件上姓氏的拼音'],
    #     ['answer', '请输入您证件上姓氏的拼音']
    # )
    # @unpack
    # def test_10_lastname_error(self, lastname, lastname_error_message):
    #     """lastname error"""
    #     self.page.lastName_input.clear()
    #     self.page.lastName_input.send_keys(lastname)
    #     self.page.city_input.click()
    #     self.assertEqual(self.page.lastName_right.text, lastname_error_message)

    # @data(
    #     ['', '请输入中文名字'],
    #     ['test', '请输入中文名字'],
    #     [111, '请输入中文名字'],
    #     ['中文名', '请输入中文名字']
    # )
    # @unpack
    # def test_11_chinesename_error(self, chinesename, chinesename_error_message):
    #     """chinesename error"""
    #     self.page.nickName_input.clear()
    #     self.page.nickName_input.send_keys(chinesename)
    #     self.assertEqual(self.page.nickName_right.text, chinesename_error_message)

    # @data(
    #     ['', '请输入真实有效的证件号码', '', '请输入真实有效的证件号码', '', '请输入真实有效的证件号码',],
    #     ['', '请输入真实有效的证件号码', '', '请输入真实有效的证件号码', '', '请输入真实有效的证件号码',],
    #     ['', '请输入真实有效的证件号码', '', '请输入真实有效的证件号码', '', '请输入真实有效的证件号码',]
    # )
    # @unpack
    # def test_12_identity_error(self, id, id_error_message, passport, passport_error_message, drivers_license, drivers_license_error_message):
    #     """证件"""
    #     # 身份证
    #     self.page.papers_num_input.send_keys(id)
    #     self.assertEqual(self.page.papers_num_right.text, id_error_message)
    #     # 护照
    #     self.page.papers_type_checkbox.click()
    #     self.page.papers_num_input.send_keys(passport)
    #     self.assertEqual(self.page.papers_num_right.text, passport_error_message)
    #     # 驾驶证
    #     self.page.drivers_license_checkbox.click()
    #     self.page.papers_num_input.send_keys(drivers_license)
    #     self.assertEqual(self.page.papers_num_right.text, drivers_license_error_message)

    # @data(
    #     ['', '请输入城市'],
    #     [111, '请输入城市'],  
    #     ['shenzhen', '请输入城市']
    # )
    # @unpack
    # def test_13_city_error(self, city, city_name_error):
    #     """city error"""
    #     self.page.city_input.clear()
    #     self.page.city_input.send_keys(city)
    #     self.assertEqual(self.page.city_right.text, city_name_error)

    # @data(
    #     ['', '请输入住宅地址']
    # )
    # @unpack
    # def test_14_address_error(self, address, address_error_message):
    #     """address error"""
    #     self.page.address_input.clear()
    #     self.page.address_input.send_keys(address)
    #     self.assertEqual(self.page.address_right.text, address_error_message)

    # @data(
    #     ['', '请输入居住年期']
    # )
    # @unpack
    # def test_15_address_date_error(self, address_date, address_date_error_message):
    #     """address date error"""
    #     self.page.addressDate_input.clear()
    #     self.page.addressDate_input.send_keys(address_date)
    #     self.assertEqual(self.page.addressDate_right.text, address_date_error_message)

    # @data(
    #     ['', '请输入职位']
    # )
    # @unpack
    # def test_16_position_error(self, position, position_error_message):
    #     """position error"""
    #     self.page.position_input.clear()
    #     self.page.position_input.send_keys(position)
    #     self.assertEqual(self.page.position_right.text, position_error_message)

    # @data(
    #     ['', '请输入现雇主名称']
    # )
    # @unpack
    # def test_17_employername_error(self, employername, employername_error_message):
    #     """employername error""" 
    #     self.page.employerName_input.clear()
    #     self.page.employerName_input.send_keys(employername)
    #     self.assertEqual(self.page.employerName_right.text, employername_error_message)

    def trarDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main()