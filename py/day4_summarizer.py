import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

try:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": f"다음 글을 3줄로 요약해줘:\n\n{text}"}
        ]
    )

    print(response.content[0].text)

except Exception as e:
    print(f"Error occurred: {e}")