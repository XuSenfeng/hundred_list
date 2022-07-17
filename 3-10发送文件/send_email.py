import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

con = smtplib.SMTP_SSL("smtp.163.com", 465)
con.login('jiao_hao_yang@163.com', 'TXOCTZRMRBZJRHSR')
# 邮件的对象
mail_obj = MIMEMultipart()
mail_header = Header('邮件自动发送测试', 'utf-8').encode()
mail_obj["Subject"] = mail_header
mail_obj["From"] = 'Jiao_Hao_yang@163.com <Jiao_Hao_yang@163.com>'
mail_obj['To'] = '1458612070@qq.com, 2648466390@qq.com, 1745887490@qq.com'

mail_text = MIMEText("这是一份自动发送的邮件", 'plain', 'utf-8')
mail_obj.attach(mail_text)

con.sendmail('Jiao_Hao_yang@163.com', ['1458612070@qq.com', '2648466390@qq.com',
                                       '1745887490@qq.com'], mail_obj.as_string())
con.quit()
print("结束")





