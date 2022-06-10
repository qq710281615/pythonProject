import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(content):
    host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
    sender_qq = '710281615@qq.com'  # 发件人邮箱
    pwd = ''
    receiver = '710281615@qq.com'

    mail_title = 'Python自动发送html格式的邮件'  # 邮件标题
    msg = MIMEMultipart()
    msg.attach(MIMEText(content, 'html', 'utf_8'))
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    msg["To"] = Header(receiver, "utf-8")
    try:
        smtp = smtplib.SMTP_SSL(host_server)  # ssl登录连接到邮件服务器
        # smtp.set_debuglevel(1)  # 0是关闭，1是开启debug
        # smtp.ehlo(host_server)  # 跟服务器打招呼，告诉它我们准备连接，最好加上这行代码
        smtp.login(sender_qq, pwd)
        smtp.sendmail(sender_qq, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")


if __name__ == '__main__':
    send_email("http://127.0.0.1:5000/static/2022-06-07/index.html")
