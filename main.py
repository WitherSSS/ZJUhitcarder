from daka import DaKa
from halo import Halo
from apscheduler.schedulers.blocking import BlockingScheduler
import getpass
import time
import datetime
import os
import sys
import requests
import json
import re
import smtplib
from email.mime.text import MIMEText

mailto_list = ["***@***.com"]
mail_host = "smtp.***.com"  # 设置服务器
mail_user = "*****"  # 用户名
mail_pass = "******"  # 口令
mail_postfix = "***.com"  # 发件箱的后缀


def doDaka(username, password):
    print("🚌 打卡任务启动")
    dk = DaKa(username, password)
    try:
        dk.login()
    except Exception as err:
        message = str(err)
        return message

    print('正在获取个人信息...')
    try:
        dk.get_info()
    except Exception as err:
        print('获取信息失败，请手动打卡，更多信息: ' + str(err))
        message = '获取信息失败，请手动打卡，更多信息: ' + str(err)
        return message

    try:
        res = dk.post()
        if str(res['e']) == '0':
            print('打卡成功')
            message = '打卡成功'
        else:
            print(res['m'])
            message = res['m']
    except:
        print('数据提交失败')
        message = '数据提交失败'
        return message
    return message

def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    me = "< "+mail_user+"@"+mail_postfix+">"  
    # 创建一个实例，这里设置为html格式邮件
    msg = MIMEText(content, _subtype='html', _charset='gb2312')
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False


def main():
    if os.path.exists('./config.json'):
        configs = json.loads(open('./config.json', 'r').read())
        users = configs["users"]
    else:
        print('⚠️未在当前目录下检测到配置文件')
        return

    for user in users:
        message = doDaka(user["username"], user["password"])
        if send_mail(user["email"], "ZJU健康打卡", message):
            print(user["username"]+"发送成功")
        else:
            print(user["username"]+"发送失败")

if __name__ == "__main__":
    main()