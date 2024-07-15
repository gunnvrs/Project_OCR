import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from tkinter import Tk, filedialog
from pythainlp.tokenize import word_tokenize
import os
import PyPDF2

# ตั้งค่าตำแหน่งของ tesseract ถ้าจำเป็น
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# ฟังก์ชันสำหรับเลือกไฟล์ PDF
def select_pdf_file():
    Tk().withdraw()  # ปิดหน้าต่างหลักของ Tkinter
    file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
    return file_path

# ฟังก์ชันสำหรับเลือก directory
def select_output_directory():
    Tk().withdraw()  # ปิดหน้าต่างหลักของ Tkinter
    directory = filedialog.askdirectory(title="Select output directory")
    return directory

# ฟังก์ชันสำหรับทำ OCR และแบ่งวรรคคำ
def ocr_and_tokenize(image_path, output_dir, page_num):
    # เปิดไฟล์รูปภาพ
    img = Image.open(image_path)

    # ทำ OCR สำหรับภาษาไทยและอังกฤษ
    text = pytesseract.image_to_string(img, lang='tha+eng')

    # ตัดคำในข้อความภาษาไทย
    words = word_tokenize(text, engine='newmm')

    # สร้างชื่อไฟล์ผลลัพธ์
    output_file_name = f"output_page_{page_num}.txt"
    output_file_path = os.path.join(output_dir, output_file_name)

    # บันทึกผลลัพธ์ลงในไฟล์
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write("ข้อความที่ได้จากการ OCR:\n")
        f.write(text)
        f.write("\n\nข้อความที่ตัดคำแล้ว:\n")
        f.write(" ".join(words))

    print(f"ผลลัพธ์ถูกบันทึกที่: {output_file_path}")

if __name__ == "__main__":
    pdf_file = select_pdf_file()
    if pdf_file:
        output_dir = select_output_directory()
        if output_dir:
            # แปลงหน้า PDF เป็นภาพ
            images = convert_from_path(pdf_file)

            for i, image in enumerate(images):
                # บันทึกภาพจากแต่ละหน้าเป็นไฟล์ชั่วคราว
                temp_image_path = f"page_{i + 1}.png"
                image.save(temp_image_path, 'PNG')

                # ทำ OCR และแบ่งวรรคคำ
                ocr_and_tokenize(temp_image_path, output_dir, i + 1)

                # ลบไฟล์ภาพชั่วคราว
                os.remove(temp_image_path)
        else:
            print("No output directory selected.")
    else:
        print("No PDF file selected.")



#_______________________ IMPROVE PERFORMANCE _______________________________

# import pytesseract
# from PIL import Image
# from pdf2image import convert_from_path
# from tkinter import Tk, filedialog
# from pythainlp.tokenize import word_tokenize
# import os

# # ตั้งค่าตำแหน่งของ tesseract ถ้าจำเป็น
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# # ฟังก์ชันสำหรับเลือกไฟล์ PDF
# def select_pdf_file():
#     Tk().withdraw()  # ปิดหน้าต่างหลักของ Tkinter
#     file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
#     return file_path

# # ฟังก์ชันสำหรับเลือก directory
# def select_output_directory():
#     Tk().withdraw()  # ปิดหน้าต่างหลักของ Tkinter
#     directory = filedialog.askdirectory(title="Select output directory")
#     return directory

# # ฟังก์ชันสำหรับทำ OCR และแบ่งวรรคคำ
# def ocr_and_tokenize(image_path, output_dir, page_num):
#     # เปิดไฟล์รูปภาพ
#     img = Image.open(image_path)

#     # ทำ OCR สำหรับภาษาไทยและอังกฤษ
#     text = pytesseract.image_to_string(img, lang='tha+eng')

#     # ตัดคำในข้อความภาษาไทย
#     words = word_tokenize(text, engine='newmm')

#     # สร้างชื่อไฟล์ผลลัพธ์
#     output_file_name = f"output_page_{page_num}.txt"
#     output_file_path = os.path.join(output_dir, output_file_name)

#     # บันทึกผลลัพธ์ลงในไฟล์
#     with open(output_file_path, "w", encoding="utf-8") as f:
#         f.write("ข้อความที่ได้จากการ OCR:\n")
#         f.write(text)
#         f.write("\n\nข้อความที่ตัดคำแล้ว:\n")
#         f.write(" ".join(words))

#     print(f"ผลลัพธ์ถูกบันทึกที่: {output_file_path}")

# if __name__ == "__main__":
#     pdf_file = select_pdf_file()
#     if pdf_file:
#         output_dir = select_output_directory()
#         if output_dir:
#             # แปลงหน้า PDF เป็นภาพครั้งละ 10 หน้า
#             page_chunks = 10
#             page_number = 1

#             for page_chunk in range(0, len(convert_from_path(pdf_file)), page_chunks):
#                 images = convert_from_path(pdf_file, first_page=page_chunk + 1, last_page=min(page_chunk + page_chunks, len(convert_from_path(pdf_file))))

#                 for i, image in enumerate(images):
#                     # บันทึกภาพจากแต่ละหน้าเป็นไฟล์ชั่วคราว
#                     temp_image_path = f"page_{page_number}.png"
#                     image.save(temp_image_path, 'PNG')

#                     # ทำ OCR และแบ่งวรรคคำ
#                     ocr_and_tokenize(temp_image_path, output_dir, page_number)

#                     # ลบไฟล์ภาพชั่วคราว
#                     os.remove(temp_image_path)
#                     page_number += 1
#         else:
#             print("No output directory selected.")
#     else:
#         print("No PDF file selected.")
