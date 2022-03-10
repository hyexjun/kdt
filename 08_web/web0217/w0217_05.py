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
# recvEmail = "onulee@naver.com"
recvEmails = ['horim159456@naver.com', 'vawav@naver.com', 'swaq11@naver.com']


title = "행운의 편지"
content = """이 편지는 영국에서 최초로 시작되어 일년에 한바퀴를 돌면서 받는 사람에게 행운을 주었고 지금은 당신에게로 옮겨진 이 편지는 4일 안에 당신 곁을 떠나야 합니다. 이 편지를 포함해서 7통을 행운이 필요한 사람에게 보내 주셔야 합니다. 복사를 해도 좋습니다. 혹 미신이라 하실지 모르지만 사실입니다.

영국에서 HGXWCH이라는 사람은 1930년에 이 편지를 받았습니다. 그는 비서에게 복사해서 보내라고 했습니다. 며칠 뒤에 복권이 당첨되어 20억을 받았습니다. 어떤 이는 이 편지를 받았으나 96시간 이내 자신의 손에서 떠나야 한다는 사실을 잊었습니다. 그는 곧 사직되었습니다. 나중에야 이 사실을 알고 7통의 편지를 보냈는데 다시 좋은 직장을 얻었습니다. 미국의 케네디 대통령은 이 편지를 받았지만 그냥 버렸습니다. 결국 9일 후 그는 암살당했습니다. 기억해 주세요. 이 편지를 보내면 7년의 행운이 있을 것이고 그렇지 않으면 3년의 불행이 있을 것입니다. 그리고 이 편지를 버리거나 낙서를 해서는 절대로 안됩니다. 7통입니다. 이 편지를 받은 사람은 행운이 깃들것입니다. 힘들겠지만 좋은게 좋다고 생각하세요. 7년의 행운을 빌면서..."""

for recvEmail in recvEmails :
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