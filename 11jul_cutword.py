##ตัดคำ
import pythainlp
from pythainlp.tokenize import word_tokenize

# ข้อความที่ได้จากการ OCR
text = "ข้อความที่ได้จากการ OCR"

# ตัดคำในข้อความภาษาไทย
words = word_tokenize(text, engine='newmm')

print(" ".join(words))
