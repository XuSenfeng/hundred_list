# 此处发送的是一个文件
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time


def send_email():
    con = smtplib.SMTP_SSL("smtp.qq.com", 465)
    con.login('1458612070@qq.com', 'txqokphlmenvfjgb')
    # 邮件的对象
    mail_obj = MIMEMultipart()
    # 添加头文件
    mail_header = Header('文件发送', 'utf-8').encode()
    mail_obj["Subject"] = mail_header
    mail_obj["From"] = '1458612070@qq.com <1458612070@qq.com>'
    mail_obj['To'] = '1745887490@qq.com'
    # 设置一段普通文本
    html_content = """
    <div>
    <h2>去搜索<h2>
    <h3><a href="http://www.baidu.com">打开百度</a></h3>
    </div>
    <div>
    <image src="cid:img_src"></image>
    </div>
    """
    html = MIMEText(html_content, 'html', "utf-8")
    # 把图片加入到网址中
    mail_obj.attach(html)
    with open("1.jpg", 'rb') as f:
        img = f.read()
        img_src = MIMEImage(img)
        img_src.add_header('Content-ID', '<img_src>')
        mail_obj.attach(img_src)
    # 发送一张图片
    with open("1.jpg", 'rb') as f:
        img2 = f.read()
        img_2 = MIMEImage(img2)
        img_2['Content-Disposition'] = 'attachment;filename = "1.jpg"'

        mail_obj.attach(img_2)


    con.sendmail('1458612070@qq.com', ['1745887490@qq.com'], mail_obj.as_string())
    con.quit()
    print("结束")


def func():
    print("{}执行func".format(time.strftime('%H:%M', time.localtime())))


if __name__ == '__main__':
    # 每分钟自动发送邮件
    schedule.every(1).minutes.do(send_email)
    while True:
        schedule.run_pending()
        time.sleep(1)
