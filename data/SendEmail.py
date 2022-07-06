from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.utils import formataddr
import configparser
from config import setting
from data import new_report
from smtplib import SMTP_SSL
from  email.mime.image import MIMEImage
class SendEmailUtil():
    def sendemail(self,subject,content):
        conn=configparser.ConfigParser()
        conn.read(setting.Config_Path,encoding="utf-8")
        from_name=conn.get("EmailData","from_name")
        from_user=conn.get("EmailData","from_user")
        to_name=conn.get("EmailData","to_name")
        to_user=conn.get("EmailData","to_user")
        passwd=conn.get("EmailData","passwd")
        server=conn.get("EmailData","server")
        port=conn.getint("EmailData","port")
        msg=MIMEMultipart('mixed')
        msg["From"]=formataddr((from_name,from_user))
        msg["To"]=formataddr((to_name,to_user))
        msg["Subject"]=subject
        report=new_report.new_report(setting.TestResult_DIR)
        f=open(report, 'rb')
        mail_body = f.read()
        f.close()

        #txt文本
        att=MIMEText(content,"plain","utf-8")
        msg.attach(att)

        #html附件
        att1 = MIMEText(mail_body, 'html', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1.add_header("Content-Disposition", "attachment", filename=("gbk", "",report.split("/")[-1]))
        msg.attach(att1)

        #html格式文本
        att2=MIMEText(mail_body,'html','utf-8')
        msg.attach(att2)

        #xlsx附件
        xlsx_path = setting.TestCase_Path
        xlsx_name = xlsx_path.split("/")[-1]
        sendfile=open(xlsx_path,"rb").read()
        att3=MIMEApplication(sendfile)
        att3["Content-Type"] = 'application/octet-stream'
        att3.add_header('Content-Disposition', 'attachment', filename=("gbk","",xlsx_name))
        msg.attach(att3)






        try:
            send_server=SMTP_SSL(server,port)
            send_server.login(from_user,passwd)
            send_server.sendmail(from_user,[to_user,],msg.as_string())
            print("发送成功")
        except:
            print("发送失败")


