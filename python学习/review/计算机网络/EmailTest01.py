# python learing
# author:TNT
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():

    sender = '1292217724@qq.com'
    receivers = ['869964523@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('张传龙', 'utf-8')
    message['To'] = Header('潘苗', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper =SMTP('smtp.qq.com',25)
    # 请自行修改下面的登录口令
    # vvnjmyqxefpkihje
    smtper.login(sender, 'vvnjmyqxefpkihje')
    print(smtper.sendmail(sender, receivers, message.as_string()))

    print('邮件发送完成!')


if __name__ == '__main__':
    main()