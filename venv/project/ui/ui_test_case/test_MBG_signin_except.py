import unittest
import time
import datetime
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.signinuser_page import UserSignIn_Page
from selenium.webdriver.common.action_chains import ActionChains
from poium import Page, PageElement, PageSelect
from testdata.read_excel import get_testdata


# # 指定 excel 文件路径
# excel_file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '//' + 'testdata' + '//' + 'signin_testdata_new.xlsx'
# # 获取列表中的数据
# # 1，2 = 获取第1行（从1开始算，不包括第2行）；0， 4 = 获取前4列（从0开始算，不包括第4列）
# signinuser_1_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 2, 0, 4)
# # 获取第1行4到19列
# signinuser_2_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 2, 4, 19)
# # 获取第1行19到21列
# signinuser_3_testdata = get_testdata(excel_file_dir, 'Sheet1', 1, 2, 19, 21)


@ddt
class SigninUser_test(unittest.TestCase):
    """
    测试注册 MBG demo 客户，异常测试用例
    """
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

    def setUp(self):
        pass

    def signinuser_1(self, email, password, password2, phone):
        """注册demo用户步骤1"""
        # time.sleep(2)
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
        self.page.affiliate_code_input.clear()
        # 已阅读
        self.page.agreement1_checkbox.click()
        # 我同意
        self.page.isOptOut_checkbox.click()
        # 点击注册
        self.page.signin_button.click()
        time.sleep(5)
        # 点击完善资料并开立真实账户按钮
        self.page.demo_up_info_button.click()


    def signinuser_2(self, surName, lastName, nickName, papers_num, birthday, city, address, addressDate, addressEn, position, employerName, incomeComment):
        """注册demo用户步骤2"""

        # step2_message_list = []
        # re_login_name = self.page.login_name_span.text
        # re_email = self.page.email_input.get_attribute('value')
        # re_phone = self.page.phone_input.get_attribute('value')
        # step2_message_list.append(re_login_name)
        # step2_message_list.append(re_email)
        # step2_message_list.append(re_phone)

        # message_list.append(re_alert_message)
        # 选择账户类型-专业账户开户
        # PageSelect(self.page.accountType_select, value='7-E00')
        # 选择称谓-男士
        PageSelect(self.page.title_select, value='1')
        # 输入-名
        self.page.surName_input.clear()
        self.page.surName_input.send_keys(surName)
        # 输入-姓
        self.page.lastName_input.clear()
        self.page.lastName_input.send_keys(lastName)
        time.sleep(1)
        # 输入中文名
        self.page.nickName_input.clear()
        self.page.nickName_input.send_keys(nickName)
        # 选择证件类型-护照
        self.page.papers_type_checkbox.click()
        # 输入证件号码
        self.page.papers_num_input.clear()
        self.page.papers_num_input.send_keys(int(papers_num))
        # 输入出生日期
        self.page.birthday_input.clear()
        self.page.birthday_input.send_keys(birthday)
        # 输入城市
        self.page.city_input.clear()
        self.page.city_input.send_keys(city)
        # 输入住宅地址
        self.page.address_input.clear()      
        self.page.address_input.send_keys(address)
        # 输入居住年期
        self.page.addressDate_input.clear()
        self.page.addressDate_input.send_keys(int(addressDate))
        # 输入住宅地址英文
        # self.page.addressEn_input.clear()
        # self.page.addressEn_input.send_keys(addressEn)
        # 选择 外汇/CFD投资经验 1-3年
        PageSelect(self.page.forExp_select, value='2')
        # 选择 OTC外汇/CFD投资频率 每周
        PageSelect(self.page.investFreq_select, value='2')
        # 选择 其他投资经验 无
        PageSelect(self.page.otherExp_select, value='1')
        # 选择 投资目标
        self.page.increase_checkbox.click()
        # 选择 是否政治人物 否
        self.page.politician_checkbox_2.click()
        # 选择 是否居住国家以外的纳税居民 否
        self.page.taxpayer_checkbox_2.click()
        # 选择 是否美国所得税纳税范围内的“美国人士” 否
        self.page.American_checkbox_2.click()
        # 选择 代表“美国人士”行事 否
        self.page.representative_checkbox_2.click()
        # 选择 美国收入的非美国人士 否
        self.page.income_checkbox_2.click()
        # 就业状况 选择 兼职
        PageSelect(self.page.employment_select, value='2')
        # 行业 选择 
        PageSelect(self.page.business_select, value='10')
        # 输入 职位
        self.page.position_input.clear()
        self.page.position_input.send_keys(position)
        # 输入现雇主名称
        self.page.employerName_input.clear()
        self.page.employerName_input.send_keys(employerName)
        # 收入来源 选择 其他
        PageSelect(self.page.incomeSource_select, value='6')
        # 年收入选择 $25,000-$49,999
        PageSelect(self.page.annual_income_select, value='2')
        # 注明其他
        self.page.incomeComment_input.send_keys(incomeComment)
        # 资产净值总和选择 $25,000-$49,999
        PageSelect(self.page.netAsset_select, value='2')
        # 确认
        self.page.agreement7_checkbox.click()
        self.page.agreement8_checkbox.click()
        self.page.agreement9_checkbox.click()
        self.page.agreement6_checkbox.click()
        self.page.agreement10_checkbox.click()
        self.page.agreement2_checkbox.click()
        self.page.agreement5_checkbox.click()
        self.page.agreement4_checkbox.click()
        self.page.agreement3_checkbox.click()

        # 确认风险披露
        self.page.riskWarn1_checkbox.click()
        self.page.riskWarn2_checkbox.click()
        self.page.riskWarn3_checkbox.click()
        self.page.riskWarn4_checkbox.click()
        # 输入留言
        self.page.message_input.send_keys('test')
        # 点击提交按钮
        time.sleep(3)
        self.page.submit_button.click()
        
        # return step2_message_list

    def signinuesr_3(self):
        """注册 demo 步骤 3"""
        # 获取登录成功提示信息
        # step3_message_list = []
        # re_success_message = self.page.success_message.text
        # step3_message_list.append(re_success_message)

        # 获取登录成功提示信息中的用户名
        # re_success_username = self.page.success_username.text.split(' ', 3)[-1]
        # step3_message_list.append(re_success_username)
        # 取消输入用户名和密码的 alert 
        # self.page.dismiss_alert()
        # 点击上传审核资料按钮
        self.page.uploadDocInfo_button.click()
        # 点击上传身份证按钮
        self.page.upload_idcard_button.click()
        # 进入上传身份证明表单
        # self.page.switch_to_frame("//iframe[starts-with(@id, 'fancybox-frame')]")
        self.page.switch_to_frame(self.page.upload_idcard_iframe)
        # 文件的完整路径
        dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        file_path = dir + '/' + 'testdata' + '/' + 'test_file.pdf' 
        # 直接写入文件的路径
        time.sleep(3)
        self.page.idcard_docFile_input_file.send_keys(file_path)
        # 点击上传按钮 
        time.sleep(3)
        self.page.upload_button.click()
        # 跳出上传身份证明表单
        # self.page.switch_to_frame_out()
        time.sleep(3)
        # 点击确认
        self.page.accept_alert()
        time.sleep(1)
        # 点击上传地址证明按钮
        self.page.upload_address_button.click()
        # 进入上传地址证明表单
        self.page.switch_to_frame(self.page.upload_address_iframe)
        # 点击选择文件按钮
        time.sleep(2)
        self.page.address_docFile_input.send_keys(file_path)
        # 点击上传按钮
        time.sleep(2)
        self.page.upload_button.click()
        time.sleep(3)
        # 点击确认
        self.page.accept_alert()

        # return step3_message_list


    @data(*signinuser_1_testdata)
    @unpack
    def test1_signinuser_step1(self, email, password, password2, phone):
        """测试注册demo用户第1步"""
        email_list = email.split('_', 2)
        step1_str_email = email_list[0] + '_' + email_list[1] + '_' + self.time_now + email_list[2]
        # step1_str_email = '{test_time}'.format(test_time=self.time_now) + email
        str_phone = '{test_time}'.format(test_time=self.time_now) + phone
        self.signinuser_1(step1_str_email, password, password2, str_phone)

    @data(*signinuser_2_testdata)
    @unpack
    def test2_signinuser_step2(self, login_name, re_email, re_phone, surName, lastName, nickName, papers_num, birthday, city, address, addressDate, addressEn, position, employerName, incomeComment):
        """测试注册demo用户第2步"""
        # login_name_list = login_name.split('_', 2)
        # str_login_name = login_name_list[0] + '_' + login_name_list[1] + '_' + self.time_now + login_name_list[2]
        # str_login_name = '{test_time}'.format(test_time=self.time_now) + login_name
        # re_email_list = re_email.split('_', 2)
        # str_re_email = re_email_list[0] + '_' + re_email_list[1] + '_' + self.time_now + re_email_list[2]
        # str_re_email = '{test_time}'.format(test_time=self.time_now) + re_email
        # str_re_phone = '{test_time}'.format(test_time=self.time_now) + re_phone
        # 去掉手机号首位的 0
        # new_str_re_phone = str_re_phone.lstrip('0')
        str_papers_num = papers_num + '{test_time}'.format(test_time=self.time_now)
        # step2_messages = self.signinuser_2(surName, lastName, nickName, str_papers_num, birthday, city, address, addressDate, addressEn, position, employerName, incomeComment)
        self.signinuser_2(surName, lastName, nickName, str_papers_num, birthday, city, address, addressDate, addressEn, position, employerName, incomeComment)

        # self.assertEqual(step2_messages[0], str_login_name)
        # self.assertEqual(step2_messages[1], str_re_email)
        # self.assertEqual(step2_messages[2], new_str_re_phone)

    
    @data(*signinuser_3_testdata)
    @unpack
    def test2_signinuser_step3(self, expect_message, expect_name):
        """测试注册demo用户第3步"""
        # 执行注册live用户的第3步，获取注册提示信息及提示信息中的用户名
        # expect_name_list = expect_name.split('_', 2)
        # str_expect_name = expect_name_list[0] + '_' + expect_name_list[1] + '_' + self.time_now + expect_name_list[2]
        # step3_message = self.signinuesr_3()
        self.signinuesr_3()
        # 断言注册提示信息和注册信息中的用户名是否符合预期
        # self.assertEqual(step3_message[0], expect_message)
        # self.assertEqual(step3_message[1], str_expect_name)

    def tearDown(self):
        pass
      
    @classmethod
    def tearDownClass(cls):
        """
        关闭浏览器
        """
        time.sleep(5)
        cls.dr.quit()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()