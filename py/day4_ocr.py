from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("sample_image.png")
text = pytesseract.image_to_string(image, lang='eng+kor')

print(text)