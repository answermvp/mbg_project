from poium import Page, PageElement, PageSelect
from selenium import webdriver


class Csadmin_Page(Page):
    """csadmin 页面"""
    # 登录页
    username_input = PageElement(name='account', describe='用户名')
    password_input = PageElement(name='password', describe='密码')
    submit_button = PageElement(xpath='//*[@id="login_content"]/div[1]/form/div/input', describe='登录')

    # 审核信息
    # 待审核银行信息
    bank_info = PageElement(xpath='//*[@id="info-bank"]/a', describe='待审核银行信息')
    # 待审核银行信息页面的用户名
    aetosAccount_input = PageElement(name='aetosAccount', describe='用户名')
    # 待审核银行信息页面的submit按钮
    aetosAccount_button = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/ul/li[6]/div[1]/div/button', describe='submit')
    # 待审核银行信息页面的第一行的审核按钮
    bankinfo_check_button = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[14]/div/a', describe='审核')
    # 复审通过按钮
    review2suss_button = PageElement(name='review2suss', describe='复审通过')
    # 待审核入金银行信息
    unipay_bank_info = PageElement(xpath='//*[@id="info-unipay"]/a', describe='待审核入金银行信息')
    # 待审核入金银行页面的用户名
    unipaybank_userName = PageElement(name='userName', describe='用户名')
    # 待审核入金银行页面的submit按钮
    unipaybank_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[1]/form/div/ul/li[9]/div[1]/div/button', describe='submit')
    # 待审核入金银行信息页面的第一行的审核按钮
    unipaybank_check_button = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[12]/div/a', describe='审核')
    # 待审核信用卡
    card_info = PageElement(xpath='//*[@id="info-card"]/a', describe='待审核信用卡')
    # 待审核信用卡页面的用户名
    card_username = PageElement(xpath='//*[@id="navTab"]/div[2]/div[4]/div[1]/form/div/ul/li[7]/input', describe='用户名')
    # 待审核信用卡页面的submit
    card_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[4]/div[1]/form/div/ul/li[10]/div[1]/div/button', describe='submit')
    # 待审核信用卡页面的审核按钮
    card_check = PageElement(xpath='//*[@id="navTab"]/div[2]/div[4]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[13]/div/a', describe='审核')
    # 待审核客户资料
    clt_info = PageElement(xpath='//*[@id="info-clt"]/a', describe='待审核客户资料')
    # 待审核客户资料页面的用户名
    clt_username = PageElement(xpath='//*[@id="navTab"]/div[2]/div[5]/div[1]/form/div/ul/li[5]/input', describe='用户名')
    # 待审核客户资料页面的submit
    clt_submint = PageElement(xpath='//*[@id="navTab"]/div[2]/div[5]/div[1]/form/div/ul/li[9]/div[1]/div/button', describe='submit')
    # 待审核客户资料页面的第一行的审核按钮
    clt_check_1 = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[11]/div/a', describe='审核1')
    # 点击复审通过按钮
    clt_review2suss_button = PageElement(name='review2suss', describe='复审通过') 
    clt_check_2 = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[11]/div/a', describe='审核2')
    # 待审核IB资料
    ib_info = PageElement(xpath='//*[@id="info-ib"]/a', describe='待审核IB资料')
    # 待审核IB资料页面的用户名
    ib_username = PageElement(xpath='//*[@id="pagerForm"]/div/ul/li[5]/input', describe='用户名')
    # 待审核IB资料页面的submit
    ib_submit = PageElement(xpath='//*[@id="pagerForm"]/div/ul/li[9]/div[1]/div/button', describe='submit')
    # 待审核IB资料页面的第一行的审核按钮
    ib_check = PageElement(xpath='//*[@id="navTab"]/div[2]/div[6]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[11]/div/a', describe='审核')

    # 用户列表
    user_list = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[2]/ul/li[1]/div/a', describe='用户列表')
    # 用户列表的查询按钮
    userlist_submit = PageElement(xpath='//*[@id="form_p"]/div/ul/li[19]/div[1]/div/button', describe='查询')
    # 用户列表中的第一个用户名
    # 4.2
    # username = PageElement(xpath='//*[@id="navTab"]/div[2]/div[4]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/div/a', describe='用户名')
    # 4.9
    # username = PageElement(xpath='//*[@id="navTab"]/div[2]/div[4]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/div/a', describe='用户名')
    # MBG
    username = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/div/a', describe='用户名')
    # 个人信息弹框中的交易账号
    transaction_num = PageElement(xpath='/html/body/div[13]/div[2]/div/div/div[1]/a/span', describe='交易账号')
    # 累计入金限额
    quota_select = PageElement(name='amountLimit', describe='累计入金限额')
    # 提交修改累计入金限额
    quota_submit = PageElement(xpath='/html/body/div[13]/div[2]/div/div/div[2]/form/div/div[5]/label/input', describe='提交修改')
    # 用户资料
    #user_info = PageElement(id_='doc', describe='资料')
    # 客户状态
    user_state_select = PageElement(xpath='/html/body/div[13]/div[2]/div/div/div[1]/form/div[1]/select', describe='客户状态')
    # 提交客户状态按钮
    userstate_submit = PageElement(xpath='/html/body/div[13]/div[2]/div/div/div[1]/form/div[2]/label/input')
    # userstate_submit = PageElement(xpath='//*[@id="setAppr"]/div[2]/div/input[4]', describe='提交')

    # 用户列表中的入金按钮
    in_button = PageElement(xpath='//*[@id="navTab"]/div[2]/div[4]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div/span[2]/a', describe='入')
    dp_button = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[6]/div/span[2]/a', describe='DP')
    # 入金金额
    in_num = PageElement(xpath='//*[@id="money"]', describe='入金金额')
    # 入金 comment
    comment = PageElement(id_='comment', describe='comment')
    # 入金说明
    remarks = PageElement(id_='remarks', describe='说明')
    # 入金提交
    in_submit = PageElement(xpath='//*[@id="submit"]', describe='提交')
    # 入金信息确认按钮
    in_accept = PageElement(id_='easyDialogYesBtn', describe='入金信息确认')

    # 审核IB
    check_IB = PageElement(xpath='//*[@id="info-ib"]/a', describe='待审核IB按钮')
    cleck_addre = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[11]/div/a', describe='审核地址证明')
    mbg_cleck_addre = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[10]/div/a', describe='审核地址证明')
    IB_review2suss_button = PageElement(xpath='//*[@id="review"]/div[2]/input[1]', describe='复审通过按钮')
    check_identity = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[11]/div/a', describe='审核身份证明')
    mbg_check_identity = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[10]/div/a', describe='审核身份证明')
    IB_name = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/div/a', describe='IB 用户名')
    bgm_IB_name = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/div/a', describe='IB 用户名')
    # IB_info = PageElement(xpath='/html/body/div[15]/div[2]/div/div/div[1]/a[2]/span', describe='IB信息')
    IB_info = PageElement(xpath='/html/body/div[13]/div[2]/div/div/div[1]/a[2]/span', describe='IB信息')
    # IB_state = PageElement(xpath='/html/body/div[15]/div[2]/div/form/div[1]/div/div[1]/select', describe='IB状态')
    IB_state = PageElement(xpath='/html/body/div[13]/div[2]/div/form/div[1]/div/div[1]/select', describe='IB状态')
    IB_amountLimit = PageElement(xpath='/html/body/div[13]/div[2]/div/form/div[1]/div/div[8]/select', describe='累计入金限额')
    IB_info_save = PageElement(id_='saveIb', describe='IB信息保存')
    new_client = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div', describe='new_client列的第一行')
    info = PageElement(id_='doc', describe='资料')
    ready_to_activate_alert = PageElement(id_='easyDialogYesBtn', describe='ready to activate 确定按钮')
    # info = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div/span[1]', describe='资料')
    approved = PageElement(id_='approved', describe='开启IB账号')
    affirm_button = PageElement(xpath='//*[@id="alertMsgBox"]/div[1]/div/div[2]/ul/li[1]/a/span', describe='确认开立账户')
    # IB_in = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/div/span[2]/a', describe='入')
    IB_line3_div = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[4]/div', describe='第3行的是否新客户')
    # IB_in = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/div/span[2]/a', describe='入')
    IB_in = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/div/span[2]/a', describe='入')
    bgm_IB_in = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[6]/div/span[4]/a', describe='in')
    Ib_in_money = PageElement(id_='money', describe='入金金额')
    Ib_in_comment = PageElement(id_='comment', describe='入金comment')
    Ib_in_remarks = PageElement(id_='remarks', describe='入金说明')
    Ib_in_submit = PageElement(id_='submit', describe='入金提交')
    Ib_in_accept = PageElement(id_='easyDialogYesBtn', describe='入金信息确认')
    IB_userlist_username_input = PageElement(xpath='//*[@id="form_p"]/div/ul/li[2]/input', describe='用户名输入框')
    # IB_newuser_div = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/div', describe='是否新客户')
    IB_newuser_div = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/div', describe='是否新客户')
    bgm_IB_newuser_div = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div', describe='new Client')
    bgm_IB_newuser_div_line3 = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[5]/div', describe='new Client')
    bgm_IB_line3_DP = PageElement(xpath='//*[@id="navTab"]/div[2]/div[3]/div[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[6]/div/span[2]/a', describe='用户列表第3行的 DP')
    userlist_username_input = PageElement(xpath='//*[@id="form_p"]/div/ul/li[2]/input', describe='用户列表中的Username搜索框')

    # /html/body/div[13]/div[2]/div/div/div[1]/a[2]

    # 出金流程
    log_out = PageElement(xpath='//*[@id="header"]/div/ul[1]/li[6]/a', describe='退出 csadmin')
    # 出金管理
    # step1
    chujinguanli_span = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[7]/h2', describe='出金管理')
    cs_check_a = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[8]/ul/li/div/a', describe='Cs Check')
    cs_check_username_input = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/ul/li[1]/input', describe='cs check 页面的 username')
    cs_check_username_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/div/ul/li/div[1]/div/button', describe='cs check 页面的 username 的 submit')
    cs_check_checkstatus_select = PageElement(name='changeTaskStatus', describe='Check Status')
    cs_check_comment_input = PageElement(xpath='//*[contains(@id, "comment-6")]', describe='cs check comment')
    cs_check_action_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[14]/div/div/a', describe='submit')
    # step2 
    risk_check_a = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[8]/ul/li/div/a', describe='Risk Check')
    risk_check_username_input = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/ul/li[1]/input', describe='risk check 页面的 username')
    risk_check_username_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/div/ul/li/div[1]/div/button', describe='risk check 页面的 username 的 submit')
    risk_check_checkstatus_select = PageElement(name='changeTaskStatus', describe='Check Status')
    risk_check_comment_input = PageElement(xpath='//*[contains(@id, "comment-6")]', describe='risk check comment')
    risk_check_action_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[17]/div/div/a', describe='submit')
    # step3 Settlement Check
    # (1) WD Standing Setup
    wd_standing_setup_a = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[8]/ul/li[1]/div/a', describe='wd standing setup')
    wd_standing_setup_username_input = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/ul/li[1]/input', describe='wd standing setup 页面的 username')
    wd_standing_setup_username_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/div/ul/li/div[1]/div/button', describe='wd standing setup 页面的 username 的 submit')
    wd_standing_setup_checkbox = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[1]/div/input', describe='wd standing setup 页面的 checkbox')
    wd_standing_setup_process = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[1]/ul/li/a/span', describe='wd standing setup 页面的 process')
    wd_standing_setup_alert = PageElement(xpath='//*[@id="alertMsgBox"]/div[1]/div/div[2]/ul/li[1]/a/span', describe='wd standing setup 页面的确认提交 alert')
    # (2) WD Allocation
    wd_alloction_a = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[8]/ul/li[2]/div/a', describe='wd alloction')
    wd_alloction_username_input = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/ul/li[1]/input', describe='wd alloction 页面的 username')
    wd_alloction_username_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/div/ul/li/div[1]/div/button', describe='wd alloction 页面的 username 的 submit')
    wd_alloction_item_div = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/td[4]/div', describe='wd alloction 搜索出来的数据')
    wd_alloction_allocate_span = PageElement(xpath='//*[@id="doc"]/span', describe='wd alloction 页面的 allocate 按钮')
    wd_allocions_allocate_anount_input = PageElement(xpath='//*[@id="allocateForm"]/div[8]/div[2]/div/table/tbody/tr/td[1]/div/input', describe='allocate 页面的 allocate anount 输入框')
    wd_allocions_fee_input = PageElement(xpath='//*[@id="allocateForm"]/div[8]/div[2]/div/table/tbody/tr/td[2]/div/input', describe='allocate 页面的 fee 输入框')
    wd_allocions_allocate_button = PageElement(id_='doAllocate', describe='allocate 页面的 allocate 按钮')
    # step4 Operation Check
    # (1) WD Alloc Review
    wd_alloc_review_a = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[8]/ul/li[2]/div/a', describe='wd alloc review')
    wd_alloc_review_username_input = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/ul/li[1]/input', describe='wd alloc review 页面的 username')
    wd_alloc_review_username_submit = PageElement(xpath='//*[@id="navTab"]/div[2]/div[2]/div[1]/form/div/div/ul/li/div[1]/div/button', describe='wd alloc review 页面的 username 的 submit')
    wd_alloc_review_review_a = PageElement(id_='allocationReview', describe='review 按钮')
    wd_alloc_review_confirm_button = PageElement(id_= 'reviewConfirmed', describe='confirm 按钮')
    # (2) Instruction Prepare
    instruction_prepare_a = PageElement(xpath='//*[@id="sidebar"]/div[2]/div[8]/ul/li[3]/div/a', describe='instruction prepare')
    instruction_prepare_submit = PageElement(id_='submit', describe='instruction prepare 页面的 submit')
