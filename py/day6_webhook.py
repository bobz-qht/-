from flask import Flask, request
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
GMAIL_ADDRESS = os.getenv('GMAIL_ADDRESS')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')

app = Flask(__name__)

def send_alert_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = GMAIL_ADDRESS
    msg['To'] = GMAIL_ADDRESS  # 일단 나한테 나한테 보내는 걸로 테스트

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(msg)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    print(f"웹훅 수신: {data}")

    event_type = data.get('event')

    if event_type == "urgent":
        print("🚨 긴급 알림! 확인 필요:", data)
        send_alert_email("긴급 알림", f"긴급 이벤트 발생: {data}")
    elif event_type == "form_submit":
        print("일반 폼 제출, 저장만 진행")
    else:
        print(f"알 수 없는 이벤트 타입: {event_type}")

    # 1. 기존 로그 불러오기 (파일 없으면 빈 리스트로 시작)
    try:
        with open('webhook_log.json', 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    if not isinstance(logs, list):
        logs = []

    # 2. 새 데이터를 리스트에 추가
    logs.append(data)

    # 3. 전체 리스트를 다시 저장
    with open('webhook_log.json', 'w') as f:
        json.dump(logs, f)

    return "Webhook received", 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)