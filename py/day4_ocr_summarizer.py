import os
from dotenv import load_dotenv
from anthropic import Anthropic
from PIL import Image
import pytesseract

load_dotenv()
client = Anthropic()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("sample_image.png")
text = pytesseract.image_to_string(image, lang='eng+kor')

print(text)

if not text:
    print("이미지에서 텍스트를 추출하지 못했어.")
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
