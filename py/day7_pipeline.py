import os
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request
from dotenv import load_dotenv
from supabase import create_client
from day4_summarizer import summarize_text

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

app = Flask(__name__)


def save_event(content, summary):
    supabase.table("events").insert({"content": content, "summary": summary}).execute()


def send_notification(summary):
    msg = MIMEText(f"새 이벤트가 요약되어 저장되었습니다:\n\n{summary}")
    msg["Subject"] = "새 이벤트 알림"
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = GMAIL_ADDRESS

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(msg)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    content = data.get("content", "")

    if not content:
        return {"error": "content가 없습니다"}, 400

    summary = summarize_text(content)
    save_event(content, summary)
    send_notification(summary)

    return {"status": "처리 완료", "summary": summary}


if __name__ == "__main__":
    app.run(port=5000)