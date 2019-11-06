import unittest
import time
import datetime
import os
from ddt import ddt, file_data, data, unpack
from selenium import webdriver
from pages.signinIB_page import SignInIB_Page
from selenium.webdriver.common.action_chains import ActionChains
from poium import Page, PageElement, PageSelect
from testdata.read_excel import get_testdata


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
class SigninIB_test(unittest.TestCase):
    """
    测试MBG注册IB
    使用时间戳的方式
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
        cls.page = SignInIB_Page(cls.dr)
        # 客户经理开户链接注册IB
        cls.page.get('https://trust.mbgmarkets.me/30300002-IB')
        # 时间戳，用于注册用户名拼接
        cls.time_now = str(datetime.datetime.now().strftime('%y%m%d%H%M'))


    def setUp(self):
        pass

    def signinIB_1(self, email, password, password2, phone):
        """注册IB步骤1"""
        # 输入电邮
        self.page.email_input.clear()
        self.page.email_input.send_keys(email)
        # 输入密码
        self.page.password_input.clear()
        self.page.password_input.send_keys(password)
        # 确认密码
        self.page.password2_input.clear()
        self.page.password2_input.send_keys(password2)
        # 输入手机号码
        self.page.phone_input.clear()
        self.page.phone_input.send_keys(phone)
        # 选择国家
        PageSelect(self.page.country_select, value='CN')
        # 已阅读
        self.page.agreement1_checkbox.click()
        # 我同意
        self.page.isOptOut_checkbox.click()
        # 点击注册
        self.page.signin_button.click()

    def signinIB_2(self, surName, lastName, nickName, papers_num, birthday, city, address, addressDate, addressEn, position, employerName, incomeComment):
        """注册IB步骤2"""
        # time.sleep(5)
        step2_message_list = []
        # 获取在步骤2页面中自动载入的当前登录用户名
        re_login_name = self.page.login_name_span.text
        # 获取在步骤2页面中自动载入的电邮
        re_email = self.page.email_input.get_attribute('value')
        # 获取在步骤2页面中自动载入的手机号码
        re_phone = self.page.phone_input.get_attribute('value')
        step2_message_list.append(re_login_name)
        step2_message_list.append(re_email)
        step2_message_list.append(re_phone)
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
        self.page.papers_num_input.send_keys(papers_num)
        # 输入出生日期
        self.page.birthday_input.clear()
        self.page.birthday_input.send_keys(birthday)
        # 输入城市
        self.page.city_input.clear()
        self.page.city_input.send_keys(city)
        # 输入住宅地址
        self.page.address_input.click()
        self.page.address_input.clear()      
        self.page.address_input.send_keys(address)
        # 输入居住年期
        self.page.addressDate_input.clear()
        self.page.addressDate_input.send_keys(int(addressDate))
        time.sleep(2)
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
        self.page.agreement5_checkbox.click()
        self.page.agreement2_checkbox.click()
        self.page.agreement1_checkbox.click()
        self.page.agreement3_checkbox.click()
        self.page.agreement4_checkbox.click()

        # <- 阅读条款
        # # 点击阅读
        # self.page.readed_button.click()
        # # 下拉滚动条到底部
        # # 切换到条款内容表单
        # self.page.switch_to_frame('cntIframe')
        # time.sleep(2)
        # # 使用 js 控制滚动条
        # js = '$(".scroll").scrollTop(20000)'
        # self.page.run_script(js)
        # time.sleep(2)
        # # 切换出条款内容表单
        # self.page.switch_to_frame_out()
        # # 点击我已阅读按钮
        # self.page.clause_button.click()
        # time.sleep(1)
        # 阅读条款->

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
        time.sleep(5)

        return step2_message_list


    def signinIB_3(self):
        """注册IB步骤3"""
        # 获取登录成功提示信息
        step3_message_list = []
        re_success_message = self.page.success_message.text
        step3_message_list.append(re_success_message)
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
        # time.sleep(2)
        # 往上传身份证input框内输入文件路径
        # self.page.idcard_docFile_input.send_keys(r'D:\dp\test\project\ui\testdata\test_file.pdf')
        # 修改【文件名】input 的 type 由 file 修改为 text
        # self.page.set_attribute(self.page.idcard_docFile_input, input, 'text')
        # js = 'document.getElementById("docFile").type = "text";'
        #js = 'document.querySelector("#docFile").type="text";'
        # self.page.run_script(js)
        # self.page.set_attribute('#docFile', input, 'text')
        # 文件的完整路径
        dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        file_path = dir + '/' + 'testdata' + '/' + 'test_file.pdf' 
        # # 点击文件上传框
        # time.sleep(3)
        # self.page.idcard_docFile_input_text.click()
        # 直接写入文件的路径
        time.sleep(3)
        self.page.idcard_docFile_input_file.send_keys(file_path)
        # 选择文件
        # os.system(r"D:\dp\test\project\ui\testdata\upload_file.exe chrome D:\dp\test\project\ui\testdata\test_file.pdf")
        # <-----------------------------------------------------先注释掉
        # # 当前文件的上级目录
        # dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # cmd = dir + '/' + 'testdata' + '/' + 'upload_file.exe chrome ' + dir + '/' + 'testdata' + '/' + 'test_file.pdf'
        # # 执行 cmd
        # os.system(cmd)
        # 先注释掉------------------------------------------------------->
        # 修改【文件名】input 的 type 由 text 修改为 file
        # self.page.set_attribute('#docFile', input, 'file')
        # 点击上传之前，将 type 改回 file
        #time.sleep(2)
        #js = 'document.querySelector("#docFile").type="file";'
        # self.page.run_script(js)
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
        # # 选择文件
        # # os.system(r"D:\dp\test\project\ui\testdata\upload_file.exe chrome D:\dp\test\project\ui\testdata\test_file.pdf")
        # cmd = dir + '/' + 'testdata' + '/' + 'upload_file.exe chrome ' + dir + '/' + 'testdata' + '/' + 'test_file.pdf'
        # os.system(cmd)
        # time.sleep(2)
        # 点击上传按钮
        time.sleep(2)
        self.page.upload_button.click()
        time.sleep(3)
        # 点击确认
        self.page.accept_alert()

        return step3_message_list


    # @data(
    #     ['test_answer_205@email.com', '123456789aA', '123456789aA', '999205'],
    # )
    @data(*signinib_1_testdata)
    @unpack
    def test_1_signinIB_1(self, email, password, password2, phone):
        """测试注册IB第1步"""
        email_list = email.split('_', 2)
        step1_str_email = email_list[0] + '_' + email_list[1] + '_' + self.time_now + email_list[2]
        str_phone = '{test_time}'.format(test_time=self.time_now) + phone
        self.signinIB_1(step1_str_email, password, password2, str_phone)

    @data(*signinib_2_testdata)
    @unpack
    def test_2_signinIB_2(self, expect_username, expect_email, expect_phone, surName, lastName, nickName, papers_num, birthday, city, address, addressDate, addressEn, position, employerName, incomeComment):
        """测试注册IB第2步"""
        expect_username_list = expect_username.split('_', 2)
        str_expect_username = expect_username_list[0] + '_' + expect_username_list[1] + '_' + self.time_now + expect_username_list[2]
        expect_email_list = expect_email.split('_', 2)
        str_expect_email = expect_email_list[0] + '_' + expect_email_list[1] + '_' + self.time_now + expect_email_list[2]
        str_expect_phone = '{test_time}'.format(test_time=self.time_now) + expect_phone
        # 去掉手机号首位的 0
        new_str_expect_phone = str_expect_phone.lstrip('0')
        str_papers_num = papers_num + '{test_time}'.format(test_time=self.time_now)
        # 执行IB注册的第2步，获取到页面中自动载入的信息
        step2_message = self.signinIB_2(surName, lastName, nickName, str_papers_num, birthday, city, address, addressDate, addressEn, position, employerName, incomeComment)
        # 断言自动载入的信息是否符合预期
        self.assertEqual(step2_message[0], str_expect_username)
        self.assertEqual(step2_message[1], str_expect_email)
        self.assertEqual(step2_message[2], new_str_expect_phone)

    @data(*signinib_3_testdata)
    @unpack
    def test_3_signinIB_3(self, expect_message, expect_name):
        """测试注册IB第3步"""
        # expect_name_list = expect_name.split('_', 2)
        # str_expect_name = expect_name_list[0] + '_' + expect_name_list[1] + '_' + self.time_now + expect_name_list[2]
        # 执行IB注册的第3步，获取注册提示信息及提示信息中的用户名
        step3_message = self.signinIB_3()
        # 断言注册提示信息和注册信息中的用户名是否符合预期
        self.assertEqual(step3_message[0], expect_message)
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

if __name__ == '__main__':
    unittest.main()