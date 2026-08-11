import os
from dotenv import load_dotenv
from anthropic import Anthropic
from pypdf import PdfReader

load_dotenv()
client = Anthropic()


try:
    reader = PdfReader("sample_report.pdf") 

    text = ""
    for page in reader.pages:
        text += page.extract_text()
    for i, page in enumerate(reader.pages):
        text += f"\n\n--- Page {i + 1} ---\n\n"
        text += page.extract_text()

except Exception as e:
    print(f"Error occurred while reading PDF: {e}")
    text = ""

print(text)

if not text:
    print("No text extracted from the PDF.")
    exit()

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