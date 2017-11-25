#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from email import encoders

from email.header import Header

from email.mime.text import MIMEText

from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
import smtplib
import time
import os

def _format_addr(s):

    name, addr = parseaddr(s)

    return formataddr((Header(name, 'utf-8').encode(), addr))




'''
msg = MIMEText('好吧我是 Python邮件测试', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
'''
def send():
    from_addr ='sqltxt@163.com'# input('sqltxt@163.com')
    password ='iamanothwolf1999'# input('iamanothwolf1999')
    to_addr = 'sqltxt@qq.com'#input('sqltxt@qq.com')#niuhh@starfutures.com.cn
    smtp_server = 'smtp.163.com'#input('smtp.163.com')
    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('C:/Users/Administrator/Documents/tbv5321_x64_portable/'+str(int(time.strftime("%Y%m%d")))+'.fbk', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('text', 'fbk', filename='20171123.fbk')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='20171123.fbk')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    try:
        server = smtplib.SMTP(smtp_server,25)#465#994#25#587
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        #os.remove('C:/Users/Administrator/Documents/tbv5321_x64_portable/'+str(int(time.strftime("%Y%m%d")))+'.fbk')
        print ("发送成功")
    except smtplib.SMTPException:
        print ("无法发送邮件")
