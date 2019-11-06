# -*- coding: utf-8 -*-
import unittest
import os, sys, time, smtplib
import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import yagmail


str = '1:注册激活IB\n2:注册激活live\n3:注册激活直客\n4:注册激活demo\n5:all\n请选择：\n' 

def get_case_name(input_num):
    case_name =''
    input_num = int(input_num)
    if input_num == 1:
        case_name = 'test_MBG_ib_*.py'
    elif input_num == 2:
        case_name = 'test_MBG_live_*.py'
    elif input_num == 3:
        case_name = 'test_MBG_zhike_*.py'
    elif input_num == 4:
        case_name = 'test_MBG_demo*.py'
    elif input_num == 5:
        case_name = 'test_MBG_*.py'
    else:
        pass

    return case_name

# 通过命令行输入执行脚本
# name = get_case_name(int(input(str)))

# sys.argv 输入
name = get_case_name(sys.argv[1])

case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ui_test_case')

def run_case(name):
    # discover = unittest.defaultTestLoader.discover(case_path, pattern='test_MBG_ib_1_*.py', top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(case_path, pattern=name, top_level_dir=None)
    return discover

# def send_mail(file):
#     """正文的方式"""
#     f = open(file, 'rb')
#     mail_body = f.read()
#     f.close()
#     msg = MIMEText(mail_body, 'html', 'utf-8')
#     msg['Subject'] = Header('测试报告', 'utf-8')
#     smtp = smtplib.SMTP()
#     smtp.connect('imap.exmail.qq.com')
#     smtp.login('answer.du@victoria-tech.com','Dp111111')
#     smtp.sendmail('answer.du@victoria-tech.com','1826339495@qq.com', msg.as_string())
#     smtp.quit()

# def send_mail(file):123456789aA
#     """附件的方式"""123456789aA
#     # 发送邮箱服务器123456789aA
#     smtpserver = 'im123456789aA
#     # 发送邮箱用户名和密码
#     user = 'answer.du@victoria-tech.com'
#     password = 'Dp111111'
#     # 发送邮箱
#     sender = 'answer.du@victoria-tech.com'
#     # 接收邮箱
#     receiver = '1826339495@qq.com'
#     # 发送邮件主题
#     subject = '测试报告'

#     # 发送的附件
#     sendfile = open(file,'rb').read()
#     att = MIMEText(sendfile, 'base64', 'utf-8')
#     att['Content-Type'] = 'application/octet-stream'
#     att['Content-Disposition'] = "attachment; filename='report.html'"

#     msgRoot = MIMEMultipart('related')
#     msgRoot['Subject'] = subject
#     msgRoot.attach(att)

#     # 连接发送邮件
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(user,password)
#     smtp.sendmail(sender, receiver, msgRoot.as_string())
#     smtp.quit()

def send_mail(file):
    """yagmail 的方式"""
    # 连接服务器
    yag = yagmail.SMTP(user='answer.du@victoria-tech.com', password='Dp111111', host='imap.exmail.qq.com')
    # 邮件正文
    # contens = [
    #     'dear all: \n'
    #     '此次测试功能有：au 环境的注册，激活，提交出金。\n'
    #     '测试结果详情请参考附件'
    # ]
    contens = ['dear all: \n'
        '\n'
        '\t 本次执行了测试注册功能的测试用例，测试结果详情请参考附件\n'
    ]
    # 发送邮件
    # 接收邮件的邮箱
    # receive_email = ['shirly.xia@victoria-tech.com','answer.du@victoria-tech.com']
    receive_email = ['answer.du@victoria-tech.com']
    yag.send(receive_email, '自动化测试报告', contens, [file])




if __name__ == '__main__':
    # 按照一定格式获取当前时间
    now = time.strftime('%m%d_%H%M')
    # 将当前时间加入到报告文件名称中
    # filename = './test_report/' + 'test_report_' + now + '.html'
    filename = '/root/venv/project/ui/test_report/' + 'test_report_' + now + '.html'
    # 定义测试报告存放路径
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'web UI 自动化测试报告',
                description=u'测试注册功能'
        )
    runner.run(run_case(name))
    fp.close()
    send_mail(filename)





