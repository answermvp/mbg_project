from poium import Page, PageElement, PageSelect
from selenium import webdriver


class Chujin_Page(Page):
    """前台出金页面"""
    username_input = PageElement(id_='userName', describe='登录用户名')
    password_input = PageElement(id_='password', describe='登录密码')
    login_button = PageElement(id_='submit', describe='登录按钮')
    churujinguanli_a = PageElement(xpath='//*[@id="siderbar"]/dl[2]/dt/a', describe='出入金管理')
    chujin_span = PageElement(xpath='//*[@id="siderbar"]/dl[2]/dd/ul/li[2]/a/span', describe='出金')
    chujin_num_input = PageElement(id_='amount', describe='出金金额')
    login_password_input = PageElement(id_='password', describe='登录密码')
    submin_button = PageElement(id_='paySubmit', describe='提交按钮')
    affirm_button = PageElement(id_='confirmBtn', describe='确认按钮')

