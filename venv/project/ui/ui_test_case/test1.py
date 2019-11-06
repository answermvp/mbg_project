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

# from selenium import webdriver
# from time import sleep

# driver = webdriver.Remote(
# command_executor='http://127.0.0.1:4444/wd/hub',
# desired_capabilities={'browserName': 'chrome'})

# driver.get('https://www.baidu.com')
# driver.find_element_by_id("kw").send_keys("docker selenium")
# driver.find_element_by_id("su").click()
# sleep(1)
# driver.quit()

# str = '1.注册激活IB\n2.注册激活live\n3.注册激活直客\n4.注册激活demo\n5.all\n请选择：\n'

# # x = input(str)


# def test_input(x):
#     y =''
#     if x == 1:
#         y = '注册激活IB'
#     elif x == 2:
#         y = '注册激活live'
#     elif x == 3:
#         y = '注册激活直客'
#     elif x == 4:
#         y = '注册激活demo'
#     elif x ==5:
#         y = 'all'
#     else:
#         pass

#     print (y)

# test_input(x = int(input(str)))


# str = '1.注册激活IB\n2.注册激活live\n3.注册激活直客\n4.注册激活demo\n5.all\n请选择：\n'

# def case_name(input_num):
#     case_name =''
#     if input_num == 1:
#         case_name = 'test_MBG_ib_*.py'
#     elif input_num == 2:
#         case_name = 'test_MBG_live_*.py'
#     elif input_num == 3:
#         case_name = 'test_MBG_zhike_*.py'
#     elif input_num == 4:
#         case_name = 'test_MBG_demo_*.py'
#     elif input_num ==5:
#         case_name = 'test_MBG_*.py'
#     else:
#         print ('输入有误')

#     return case_name

# name = case_name(int(input(str)))

# print (type(name))

# import sys

# # print (sys.argv[0])
# # print (sys.argv[1])

# def test(input):
#     print (input)

# test(sys.argv[1])

# import requests

# r = requests.get('https://www.baidu.com')
# print (r.encoding)

# import sys

# print (type(str(sys.argv[1])))
# print (sys.argv[1])

# import unittest
# from ddt import ddt, file_data, data, unpack

# @ddt
# class Test_Ddt(unittest.TestCase):

#     def setUp(self):
#         pass

#     @data(
#         [1,1,2],
#         [1,2,3],
#         [1,3,4]
#         )
#     @unpack
#     def test_ddt(self, a, b, c):
#         d = a + b
#         print (c)
#         self.assertEqual(d, c)

#     def tearDown(self):
#         pass

# if __name__ == '__main__':
#     unittest.main()


# import ddt, data, unpack
# import unittest

# @ddt
# class DoubanTest(unittest.TestCase):
#     def setUp(self):
#         pass
#     def tearDown(self):
#         pass
#     @ddt([1,2,3,6],[2,3,4,5],[1,2,2,5])
#     @unpack
#     def test_add(self,testdata1,testdata2,testdate3,exceptdata):
#         sum=0
#         sum=testdata1+testdata2+testdate3
#         self.assertEqual(sum,exceptdata)



# @ddt
# class FooTestCase(unittest.TestCase):

#     @data([3, 2], [4, 3], [5, 3])
#     @unpack
#     def test_list_extracted_with_doc(self, first_value, second_value):
#         self.assertTrue(first_value > second_value)


# if __name__ =='__main__':
#     unittest.main()


import unittest
import ddt

@ddt.ddt
class Abc(unittest.TestCase):

    @ddt.data([23,3],[67,3])
    @ddt.unpack
    def testpd004(self,m,d):
        print(m,d)

if __name__ =='__main__':
    unittest.main()