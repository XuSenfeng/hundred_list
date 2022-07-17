# 此处发送的是一个网页
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

con = smtplib.SMTP_SSL("smtp.qq.com", 465)
con.login('1458612070@qq.com', 'txqokphlmenvfjgb')
# 邮件的对象
mail_obj = MIMEMultipart()
# 添加头文件
mail_header = Header('邮件自动发送测试', 'utf-8').encode()
mail_obj["Subject"] = mail_header
mail_obj["From"] = '1458612070@qq.com <1458612070@qq.com>'
mail_obj['To'] = 'Jiao_Hao_yang@163.com'
# 设置一段普通文本
html_content = """
    <div>
    <h2>去搜索</h2>
    <h3><a href="http://www.baidu.com">打开百度</a></h3>
    </div>
    """
mail_text = MIMEText(html_content, 'html', 'utf-8')
mail_obj.attach(mail_text)

con.sendmail('1458612070@qq.com', ['Jiao_Hao_yang@163.com'], mail_obj.as_string())
con.quit()
print("结束")





