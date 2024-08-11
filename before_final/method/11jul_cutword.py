# import pytesseract
# from PIL import Image
# from tkinter import Tk, filedialog
# from pythainlp.tokenize import word_tokenize
# import os

# # # ตั้งค่าตำแหน่งของ tesseract ถ้าจำเป็น
# # pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# # ฟังก์ชันสำหรับเลือกไฟล์ภาพ
# def select_image_file():
#     Tk().withdraw()  # ปิดหน้าต่างหลักของ Tkinter
#     file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")])
#     return file_path

# # ฟังก์ชันสำหรับเลือก directory
# def select_output_directory():
#     Tk().withdraw()  # ปิดหน้าต่างหลักของ Tkinter
#     directory = filedialog.askdirectory(title="Select output directory")
#     return directory

# # ฟังก์ชันสำหรับทำ OCR และแบ่งวรรคคำ
# def ocr_and_tokenize(image_path, output_dir):
#     # เปิดไฟล์รูปภาพ
#     img = Image.open(image_path)

#     # ทำ OCR สำหรับภาษาไทยและอังกฤษ
#     text = pytesseract.image_to_string(img, lang='tha+eng')

#     # ตัดคำในข้อความภาษาไทย
#     words = word_tokenize(text, engine='newmm')

#     # สร้างชื่อไฟล์ผลลัพธ์
#     base_name = os.path.basename(image_path)
#     output_file_name = os.path.splitext(base_name)[0] + "_output.txt"
#     output_file_path = os.path.join(output_dir, output_file_name)

#     # บันทึกผลลัพธ์ลงในไฟล์
#     with open(output_file_path, "w", encoding="utf-8") as f:
#         f.write("ข้อความที่ได้จากการ OCR:\n")
#         f.write(text)
#         f.write("\n\nข้อความที่ตัดคำแล้ว:\n")
#         f.write(" ".join(words))

#     print(f"ผลลัพธ์ถูกบันทึกที่: {output_file_path}")

# if __name__ == "__main__":
#     image_file = select_image_file()
#     if image_file:
#         output_dir = select_output_directory()
#         if output_dir:
#             ocr_and_tokenize(image_file, output_dir)
#         else:
#             print("No output directory selected.")
#     else:
#         print("No file selected.")
