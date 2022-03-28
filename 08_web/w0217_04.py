from fileinput import filename
import smtplib
from email.mime.text import MIMEText  # 메일 보낼 수 있는 메소드
from email.mime.multipart import MIMEMultipart  # 3-5줄 있어야 파일 첨부 가능
from email.mime.base import MIMEBase
from email import encoders


# smtp 관련 정보는 사용하려는 메일 계정의 설정에서 확인 가능
smtpName = "smtp.naver.com"
smtpPort = 587
sendEmail = "parkhj929@naver.com"
passWord = "nP@ssuu0rd****"
recvEmail = "onulee@naver.com"
recvEmails = ['horim159456@naver.com', 'vawav@naver.com', 'swaq11@naver.com']


title = "파이썬으로 이메일 보내기 확인"
content = "파이썬으로 이메일을 보냅니다. 파일 첨부 버전입니다."

# MIME 객체 선언
msg = MIMEMultipart('alternative')  # 파일첨부 아닐 때는 MIMEtext였나 그랬음
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title


# 메일 서버로 접속
part2 = MIMEText(content)
msg.attach(part2)
part = MIMEBase('application', "octet-stream")
with open("220217_시가총액_1-50위.csv", "rb") as f :
    part.set_payload(f.read())


encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename="220217_시가총액_1-50위.csv")

msg.attach(part)

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, passWord)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.close()