from poium import Page, PageElement, PageSelect
from selenium import webdriver


class UserSignIn_Page(Page):
    """用户注册页面"""
    language_input = PageElement(xpath='//*[@id="user-fiex"]/article/section[2]/div[1]/div')
    chinese = PageElement(xpath='//*[@id="user-fiex"]/article/section[2]/div[1]/div/a[2]')
    IBsignin_button = PageElement(xpath='//*[@id="user-fiex"]/article/section[1]/div/a[1]')
    email_input = PageElement(id_='userName')
    password_input = PageElement(id_='password')
    password2_input = PageElement(id_='password2')
    password1_message = PageElement(xpath='//*[@id="regForm"]/ul/li[3]/div[3]/label', describe='密码1的提示信息')
    phone_input = PageElement(id_='phone')
    agreement1_checkbox = PageElement(id_='agreement1')
    isOptOut_checkbox = PageElement(id_='isOptOut')
    signin_button = PageElement(id_='submitBtn')
    email_message = PageElement(xpath='//*[@id="regForm"]/ul/li[2]/div[3]/label')
    password_message = PageElement(xpath='//*[@id="regForm"]/ul/li[3]/div[3]/label')
    password2_message = PageElement(xpath='//*[@id="regForm"]/ul/li[4]/div[3]/label')
    phone_message = PageElement(xpath='//*[@id="regForm"]/ul/li[5]/div[3]/label')
    country_select = PageElement(id_='country', describe='国家')
    affiliate_code_input = PageElement(id_='introducer', describe='交易编码')
    # country_error_alert = PageElement(id_='guide', describe='选择国家错误弹框')
    # country_error_alert = PageElement(xpath='/html/body/div[2]/div/div', describe='选择国家错误弹框')
    # country_error_alert = PageElement(xpath='//*[@id="guide"]/p/text()[1]', describe='选择国家错误弹框')
    # country_error_alert = PageElement(xpath='//*[@id="guide"]/p', describe='选择国家错误弹框')
    country_error_alert = PageElement(xpath='//*[@id="guide"]/p/text()[1]', describe='选择国家错误弹框')
    country_error_button = PageElement(xpath='//*[@id="guide"]/div/button', describe='选择国家错误弹框的取消按钮')
    country_right = PageElement(xpath='//*[@id="regForm"]/ul/li[6]/div[3]/label', describe='国家选择框右侧的错误提示信息')
    # country_right = PageElement(class_name='g-tip-txt', describe='国家选择框右侧的错误提示信息')
    error_info = PageElement(xpath='//*[@id="countryTip"]/p', describe='国家选择框下方的提示信息')
    # step2
    login_name_span = PageElement(id_='js_loginName', describe='当前登陆用户')
    accountType_select = PageElement(id_='accountType', describe='账户类型')
    title_select = PageElement(id_='title', describe='称谓')
    surName_input = PageElement(id_='surName', describe='名')
    surName_right = PageElement(xpath='//*[@id="step03"]/ul/li[3]/div[3]/label', describe='名右侧的提示信息')
    lastName_input = PageElement(id_='lastName', describe='姓')
    lastName_right = PageElement(xpath='//*[@id="step03"]/ul/li[4]/div[3]/label', describe='姓右侧的提示信息')
    nickName_input = PageElement(id_='nickName', describe='中文名字')
    nickName_right = PageElement(xpath='//*[@id="step03"]/ul/li[5]/div[3]/label', describe='中文名右侧的提示信息')
    papers_type_checkbox = PageElement(xpath='//*[@id="goIdentityOthers"]/label[2]/input', describe='证件类型-护照')
    drivers_license_checkbox = PageElement(xpath='//*[@id="goIdentityOthers"]/label[3]/input', describe='证件类型-驾驶证')
    papers_num_input = PageElement(id_='identity', describe='证件号码')
    papers_num_right = PageElement(xpath='//*[@id="step03"]/ul/li[7]/div[3]/label', describe='证件号码右侧的提示信息')
    birthday_input = PageElement(id_='birthday', describe='出生日期')
    city_input = PageElement(id_='city', describe='城市')
    city_right = PageElement(xpath='//*[@id="step03"]/ul/li[11]/div[3]/label', describe='城市右侧的提示信息')
    address_input = PageElement(id_='address', describe='住宅地址')
    address_right = PageElement(xpath='//*[@id="step03"]/ul/li[12]/div[3]/label', describe='住宅地址右侧的提示信息')
    addressEn_input =   PageElement(id_='addressEn', describe='住宅地址英文')
    addressDate_input = PageElement(id_='addressDate', describe='居住年期')
    addressDate_right = PageElement(xpath='//*[@id="step03"]/ul/li[14]/div[3]/label', describe='居住年期右侧的提示信息')
    home_phone_input = PageElement(id_='homePhone', describe='住宅电话号码')
    orgName_input = PageElement(id_='orgName', describe='公司名称')
    website_input = PageElement(id_='website', describe='介绍经纪商网址')
    officePhone_input = PageElement(id_='officePhone', describe='座机号码')

    # 外汇/CFD投资经验下拉框
    forExp_select = PageElement(id_='forExp', describe='外汇/CFD投资经验')

    # OTC外汇/CFD投资频率下拉框
    investFreq_select = PageElement(id_='investFreq', describe='外汇/CFD投资经验')

    # 其他投资经验下拉框
    otherExp_select = PageElement(id_='otherExp', describe='其他投资经验')

    # 投资目标
    # 收益
    earnings_checkbox = PageElement(xpath='//*[@id="step04"]/ul/li[4]/div[2]/div[1]/label/input')
    # 增长
    increase_checkbox = PageElement(xpath='//*[@id="step04"]/ul/li[4]/div[2]/div[2]/label/input')
    # 投机
    speculate_checkbox = PageElement(xpath='//*[@id="step04"]/ul/li[4]/div[2]/div[3]/label/input')

    # 特别事项
    # 是政治人物
    politician_checkbox_1 = PageElement(xpath='//*[@id="step05"]/ul/li[1]/div[2]/div[1]/label[1]/input')
    # 不是政治人物
    politician_checkbox_2 = PageElement(xpath='//*[@id="step05"]/ul/li[1]/div[2]/div[1]/label[2]/input')
    # 是否居住国家以外的纳税居民
    # 是
    taxpayer_checkbox_1 = PageElement(xpath='//*[@id="step05"]/ul/li[2]/div[2]/div[1]/label[1]/input')
    # 否
    taxpayer_checkbox_2 = PageElement(xpath='//*[@id="step05"]/ul/li[2]/div[2]/div[1]/label[2]/input')
    # 是否美国所得税纳税范围内的“美国人士”
    # 是
    American_checkbox_1 = PageElement(xpath='//*[@id="step05"]/ul/li[3]/div[2]/div[1]/label[1]/input')
    # 否
    American_checkbox_2 = PageElement(xpath='//*[@id="step05"]/ul/li[3]/div[2]/div[1]/label[2]/input')
    # 代表“美国人士”行事
    # 是
    representative_checkbox_1 = PageElement(xpath='//*[@id="step05"]/ul/li[4]/div[2]/div[1]/label[1]/input')
    # 否
    representative_checkbox_2 = PageElement(xpath='//*[@id="step05"]/ul/li[4]/div[2]/div[1]/label[2]/input')
    # 美国收入的非美国人士
    # 是
    income_checkbox_1 = PageElement(xpath='//*[@id="step05"]/ul/li[5]/div[2]/div[1]/label[1]/input')
    # 否
    income_checkbox_2 = PageElement(xpath='//*[@id="step05"]/ul/li[5]/div[2]/div[1]/label[2]/input')

    # 工作情况
    # 就业状况下拉框
    employment_select = PageElement(id_='employment')

    # 行业下拉框
    business_select = PageElement(id_='business')

    # 其他注明
    incomeComment_input = PageElement(id_='incomeComment')
    
    # 职位
    position_input = PageElement(id_='position2')
    position_right = PageElement(xpath='//*[@id="position2Div"]/div[3]/label', describe='职位右侧的提示信息')
    # 雇主名称
    employerName_input = PageElement(id_='employerName')
    employerName_right = PageElement(xpath='//*[@id="employerNameDiv"]/div[3]/label', describe='雇主名称右侧的提示信息')

    # 收入来源下拉框
    incomeSource_select = PageElement(id_='incomeSource')
    
    # 申请人财务资料
    # 年收入下拉框
    annual_income_select = PageElement(id_='income')

    # 资产净值总和下拉框
    netAsset_select = PageElement(id_='netAsset')

    # 本人确认
    agreement7_checkbox = PageElement(id_='agreement7')
    agreement8_checkbox = PageElement(id_='agreement8')
    agreement9_checkbox = PageElement(id_='agreement9')
    agreement6_checkbox = PageElement(id_='agreement6')
    agreement10_checkbox = PageElement(id_='agreement10')
    agreement5_checkbox = PageElement(id_='agreement5')
    agreement2_checkbox = PageElement(id_='agreement2')
    agreement1_checkbox = PageElement(id_='agreement1')
    agreement4_checkbox = PageElement(id_='agreement4')
    agreement3_checkbox = PageElement(id_='agreement3')

    # 点击阅读按钮
    # readed_button = PageElement(xpath='//*[@id="step08"]/div/div[2]/div[1]/a[1]')
    # au2
    au_readed_button = PageElement(xpath='//*[@id="regForm"]/fieldset[8]/div/div[1]/div/div[1]/a[1]')
    # 4.9
    # readed_button = PageElement(xpath='//*[@id="regForm"]/fieldset[8]/div/div[2]/div[1]/a[1]')
    # 直客 live
    zhike_live_readed_button = PageElement(xpath='//*[@id="regForm"]/fieldset[8]/div/div[1]/div/div[1]/a[1]')
    # MBG 直客注册 live 点击阅读按钮
    MBG_zhike_live_readed_button = PageElement(xpath='//*[@id="regForm"]/fieldset[8]/div/div[2]/div[1]/a[1]')
    # MBG 注册 demo 客户点击阅读按钮
    MBG_demo_readed_button = PageElement(xpath='//*[@id="regForm"]/fieldset[8]/div/div[2]/div[1]/a[1]')
    # mbg 注册 live 点击阅读按钮
    MBG_live_readed_button = PageElement(xpath='//*[@id="regForm"]/fieldset[8]/div/div[2]/div[1]/a[1]')
    # 条款表单
    # cntI_frame = PageElement(id_='cntIframe')
    # 条款滚动条
    read_scroll = PageElement(xpath='/html/body/div[2]')
    # 条款弹框
    read_div = PageElement(xpath='/html/body/div[3]/div')
    # 最后一条条款
    end_li = PageElement(xpath='/html/body/div[2]/div[3]/ol/li[27]/ol/li[3]')
    # 已阅读按钮
    clause_button = PageElement(id_='clause')
    # 关闭弹框
    close_button = PageElement(xpath='/html/body/div[3]/div/div/a')

    # 风险披露
    riskWarn1_checkbox = PageElement(name='riskWarn1')
    riskWarn2_checkbox = PageElement(name='riskWarn2')
    riskWarn3_checkbox = PageElement(name='riskWarn3')
    riskWarn4_checkbox = PageElement(name='riskWarn4')
    # 留言
    message_input = PageElement(id_='message')
    # 提交按钮
    submit_button = PageElement(id_='submit')

    # 注册成功提示
    success_message =   PageElement(xpath='//*[@id="content"]/article[2]/div/section[3]/h3')

    # 注册的用户名
    # success_username = PageElement(xpath='//*[@id="content"]/article[2]/div/section[3]/section[1]/p[1]/strong/label')
    success_username = PageElement(xpath='//*[@id="content"]/article[2]/div/section[3]/section[1]/p[1]/strong')

    # 上传审核资料按钮
    uploadDocInfo_button = PageElement(id_='uploadDocInfo', describe='上传审核资料按钮')
    
    # 上传身份证明按钮
    upload_idcard_button = PageElement(xpath='//*[@id="content"]/article[2]/div/section[2]/div[3]/table/tbody/tr/td[4]/a')
    # 上传身份证明的 iframe
    upload_idcard_iframe = PageElement(tag='iframe', describe='上传身份证明的 iframe')
    # 上传身份证明input框
    idcard_docFile_input = PageElement(id_='docFile', describe='上传身份证明框')
    # idcard_docFile_input = PageElement(id_='fileText', describe='上传身份证明框')
    # 选择文件按钮
    # select_file_button = PageElement(class_name='bs g-txt-border m-form-file-btn')
    # idcard_docFile_input = PageElement(xpath='//*[@id="uploadPop"]/div[2]/div[1]/ul/li[1]/div[2]/div/span')
    # 上传按钮
    upload_button = PageElement(id_='upload', describe='上传')

    # 添加出金银行账户信息按钮
    bankInfo_button = PageElement(id_='bankInfo', describe='添加')
    # 州/省
    swiftState_select = PageElement(id_='swiftState', describe='州/省')
    # 城市
    bank_city_select = PageElement(id_='swiftCity', describe='城市')
    # 收款人银行名称
    swiftBankName_select = PageElement(id_='swiftBankName', describe='收款人银行名称')
    # 收款人银行账号
    bankNumber_input = PageElement(id_='bankNumber', describe='收款人银行账号')
    # 收款人姓名
    accName_input = PageElement(id_='accName', describe='收款人姓名')
    # 确定按钮
    submitBankAccount_button = PageElement(id_='submitBankAccount', describe='确认按钮')

    # 上传地址证明按钮
    upload_address_button = PageElement(xpath='//*[@id="content"]/article[2]/div/section[2]/div[7]/table/tbody/tr/td[4]/a')
    zhike_live_upload_address_button = PageElement(xpath='//*[@id="content"]/article[2]/div/section[2]/div[5]/table/tbody/tr/td[4]/a')
    idcard_docFile_input_file = PageElement(id_='docFile', describe='上传身份证明框')
    # 上传地址证明的 iframe
    upload_address_iframe = PageElement(tag='iframe', describe='上传地址证明的 iframe')
    # 上传地址证明input框
    address_docFile_input = PageElement(id_='docFile', describe='上传地址证明框')

    # demo 用户
    demo_up_info_button = PageElement(id_='regLiveInfo', describe='完善资料并开立真实账户')

    # 异常测试用例
    # email 的提示信息

    email_error_message = PageElement(xpath='//*[@id="regForm"]/ul/li[2]/div[3]/label/text()', describe='email 的错误提示信息')
 
