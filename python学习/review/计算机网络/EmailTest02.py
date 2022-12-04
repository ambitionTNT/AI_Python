# python learing
# author:TNT
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    #创建一个带附件的邮件消息对象
    message = MIMEMultipart()


    #创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)


    #读取文件并将文件作为附件添加到邮件消息队列中

    with open('C:\\Users\\long\\Desktop\\hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        # 文件类型
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment;filename=hello.txt'
        message.attach(txt)
    with open('C:\\Users\\long\\Desktop\\22年硕士复试科目大纲.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        # 文件类型
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment;filename=22年硕士复试科目大纲.xlsx'
        message.attach(xls)

    # 创建SMTP对象
    smtper =SMTP('smtp.qq.com',25)
    # 开启安全连接
    # smtper.starttls()

    sender = '1292217724@qq.com'
    receivers = ['869964523@qq.com']
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender,'vvnjmyqxefpkihje')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')
if __name__ == '__main__':
    main()



