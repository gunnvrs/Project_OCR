import pytesseract
from PIL import Image

# กำหนด path ไปยังไฟล์ Tesseract ถ้าจำเป็น
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# เปิดไฟล์รูปภาพ
img = Image.open('path/to/your_image.png')

# ทำ OCR สำหรับภาษาไทยและอังกฤษ
text = pytesseract.image_to_string(img, lang='tha+eng')

print(text)
