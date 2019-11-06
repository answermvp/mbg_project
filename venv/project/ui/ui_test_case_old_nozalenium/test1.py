# -*- coding:utf8-*-
# import os

# # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# file_path = dir + '/' + 'testdata' + '/' + 'upload_file.exe' 
# print(file_path)

# # dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# # cmd = dir + '/' + 'testdata' + '/' + 'upload_file.exe chrome ' + dir + '/' + 'testdata' + '/' + 'test_file.pdf'

# # print(cmd)

# # 设置 type
# # set_attribute

# js = 'document.querySelector("{docFile}").setAttribute("{input}", "{text}");'


# #########################

# from selenium import webdriver
# import time


# # <--------------------------------后加的
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-extensions')
# # 隐藏 GUI
# # options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options) 
# # 后加的--------------------------------- >
# driver.maximize_window()
# driver.get("https://www.baidu.com/")
# time.sleep(3)

# driver.find_element_by_id('kw').send_keys('selenium')
# time.sleep(3)
# driver.quit()

# ###########################

# from selenium import webdriver
# chrome_capabilities ={
#     "browserName": "chrome",
#     "version": "",
#     "platform": "ANY",
#     "javascriptEnabled": True,
#     # "marionette": True,
# }
# browser = webdriver.Remote("http://192.168.80.131:5555/wd/hub", desired_capabilities=chrome_capabilities)
# browser.get("http://www.163.com")
# browser.quit()


# print ('hello')

# grid_demo.py

from selenium import webdriver
from time import sleep

driver = webdriver.Remote(
command_executor='http://127.0.0.1:4444/wd/hub',
desired_capabilities={'browserName': 'chrome'})

driver.get('https://www.baidu.com')
driver.find_element_by_id("kw").send_keys("docker selenium")
driver.find_element_by_id("su").click()
sleep(1)
driver.quit()