from poium import Page, PageElement, PageSelect
from selenium import webdriver

class Customer_Manager_Check_Page(Page):
    """客户经理跟进IB页"""
    username_input = PageElement(id_='userName', describe='用户名')
    password_input = PageElement(id_='password', describe='密码')
    login_button = PageElement(id_='submit', describe='登录')
    Client_mgmt_a = PageElement(xpath='//*[@id="siderbar"]/dl[1]/dt/a', describe='客户管理')
    intention_IB = PageElement(xpath='//*[@id="siderbar"]/dl[1]/dd/ul/li[5]/a', describe='意向IB')
    follow_up_IB = PageElement(xpath='//*[@id="siderbar"]/dl[1]/dd/ul/li[5]/ul/li[1]/a', describe='待跟进IB')
    IB_username = PageElement(xpath='//*[@id="unfollowIbListBody"]/tr[1]/td[4]/a', describe='IB用户名')
    IB_info_iframe = PageElement(id_='listDetailFrame', describe='IB信息iframe')
    IB_grade_select = PageElement(id_='agentType', describe='IB等级')
    save_button = PageElement(xpath='//*[@id="myform"]/div/input', describe='保存')
