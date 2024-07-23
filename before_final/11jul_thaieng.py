##1 #like cmd 
# import pytesseract
# from PIL import Image

# # Path to the image file
# image_path = '/Users/gunnviryasiri/Desktop/ocr/testfile/file1.jpg'  # ระบุเส้นทางแบบ absolute path

# # Path to the output text file
# output_text_file = '/Users/gunnviryasiri/Desktop/ocr/11jul_3.txt'  # ระบุเส้นทางแบบ absolute path

# # Load the image
# image = Image.open(image_path)

# # Perform OCR on the image using both Thai and English languages
# text = pytesseract.image_to_string(image, lang='tha+eng')

# # Save the extracted text to a file
# with open(output_text_file, 'w', encoding='utf-8') as f:
#     f.write(text)

# print(f'Text extracted and saved to {output_text_file}')


##2 fix1 
# import pytesseract
# from PIL import Image

# # Path to the image file
# image_path = '/Users/gunnviryasiri/Desktop/ocr/testfile/file1.jpg'

# # Path to the output text file
# output_text_file = '/Users/gunnviryasiri/Desktop/ocr/11jul_4444.txt'

# # Load the image
# image = Image.open(image_path)

# # Perform OCR on the image using both Thai and English languages
# custom_config = r'--oem 3 --psm 6'  # ตัวเลือกแก้ไขพารามิเตอร์ตามที่ต้องการ
# text = pytesseract.image_to_string(image, lang='tha+eng', config=custom_config)

# # Save the extracted text to a file
# with open(output_text_file, 'w', encoding='utf-8') as f:
#     f.write(text)

# print(f'Text extracted and saved to {output_text_file}')




##3 grayscale
# import pytesseract
# from PIL import Image
# import cv2

# # Path to the image file
# image_path = '/Users/gunnviryasiri/Desktop/ocr/testfile/file1.jpg'

# # Path to the output text file
# output_text_file = '/Users/gunnviryasiri/Desktop/ocr/11jul_5.txt'

# # Load the image
# image = Image.open(image_path)

# # Convert the image to grayscale
# gray = image.convert('L')

# # Perform OCR on the image using Thai and English languages
# text = pytesseract.image_to_string(gray, lang='tha+eng')

# # Save the extracted text to a file
# with open(output_text_file, 'w', encoding='utf-8') as f:
#     f.write(text)

# print(f'Text extracted and saved to {output_text_file}')


#รวม 2,3
import pytesseract
from PIL import Image
import cv2

# Path to the image file
image_path = '/Users/gunnviryasiri/Desktop/ocr/testfile/file1.jpg'

# Path to the output text file
output_text_file = '/Users/gunnviryasiri/Desktop/ocr/11jul_6666666.txt'

# Load the image
image = Image.open(image_path)

# Convert the image to grayscale
gray = image.convert('L')

# Perform OCR on the image using Thai and English languages
custom_config = r'--oem 3 --psm 6'  # ตัวเลือกแก้ไขพารามิเตอร์ตามที่ต้องการ รวม จากวิธี2
text = pytesseract.image_to_string(gray, lang='tha+eng')

# Save the extracted text to a file
with open(output_text_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Text extracted and saved to {output_text_file}')