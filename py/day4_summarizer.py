import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

def summarize_text(text):
    """텍스트를 받아서 3줄 요약을 리턴하는 함수"""
    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": f"다음 글을 3줄로 요약해줘:\n\n{text}"}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()
    summary = summarize_text(text)
    print(summary)