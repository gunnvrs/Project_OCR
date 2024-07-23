import os
import subprocess

def convert_bmp_to_png(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".bmp"):
            bmp_path = os.path.join(directory, filename)
            png_path = os.path.splitext(bmp_path)[0] + ".png"
            subprocess.run(["convert", bmp_path, png_path])

def generate_box_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            png_path = os.path.join(directory, filename)
            base_name = os.path.splitext(png_path)[0]
            subprocess.run(["tesseract", png_path, base_name, "-l", "tha", "--psm", "6", "batch.nochop", "makebox"])

def train_model(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            png_path = os.path.join(directory, filename)
            box_path = os.path.splitext(png_path)[0] + ".box"
            subprocess.run(["tesseract", png_path, box_path, "lstm.train"])

def extract_unicharset(directory):
    box_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".box")]
    subprocess.run(["unicharset_extractor", "--norm_mode", "3"] + box_files)

def combine_tessdata(tessdata_path, output_path):
    subprocess.run(["combine_tessdata", "-e", tessdata_path, output_path])

def main():
    # กำหนดเส้นทางโฟลเดอร์
    directory = "/Users/gunnviryasiri/Desktop/ocr/ThaiOCR/ThaiOCR-TrainigSet"  # แก้ไขเส้นทางนี้ให้ตรงกับตำแหน่งที่เก็บข้อมูล
    tessdata_path = "/Users/gunnviryasiri/pythainlp-data/tessdata/tha.traineddata"  # เส้นทางไปยังไฟล์ tha.traineddata
    output_path = "tha.lstm"

    # แปลงไฟล์ BMP เป็น PNG
    convert_bmp_to_png(directory)

    # สร้างไฟล์ .box
    generate_box_files(directory)

    # ฝึกโมเดล
    train_model(directory)

    # สร้างไฟล์ unicharset
    extract_unicharset(directory)

    # สร้างไฟล์ training data
    combine_tessdata(tessdata_path, output_path)

    print("Training completed successfully!")

if __name__ == "__main__":
    main()



# import pytesseract
# from PIL import Image

# # ตั้งค่าเส้นทางให้ Tesseract ใช้โมเดลที่ฝึกเสร็จแล้ว
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# custom_config = r'--tessdata-dir "/Users/gunnviryasiri/pythainlp-data/tessdata" -l tha'

# # โหลดรูปภาพที่ต้องการทดสอบ OCR
# image_path = '/path/to/your/test/image.png'  # แก้ไขเส้นทางให้ตรงกับไฟล์ที่ต้องการทดสอบ
# image = Image.open(image_path)

# # ทำ OCR ด้วย Tesseract
# text = pytesseract.image_to_string(image, config=custom_config)

# print(text)

