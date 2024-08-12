from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

# ตั้งค่าตำแหน่งการอัปโหลดและบันทึกไฟล์
UPLOAD_FOLDER = 'static/uploads/'
PROCESSED_FOLDER = 'processed/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# หน้าแรกสำหรับอัปโหลดไฟล์
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # รับไฟล์จากผู้ใช้
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # ทำ OCR
            image = Image.open(filepath)
            text = pytesseract.image_to_string(image, lang='tha+eng')

            # บันทึกผลลัพธ์ OCR
            output_text_file = os.path.join(app.config['PROCESSED_FOLDER'], 'FORTEST.txt')
            with open(output_text_file, 'w', encoding='utf-8') as f:
                f.write(text)

            return redirect(url_for('display_file', filename=file.filename))
    return render_template('index.html')

# แสดงผลภาพและข้อความ OCR
@app.route('/display/<filename>')
def display_file(filename):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    text_file = os.path.join(app.config['PROCESSED_FOLDER'], 'FORTEST.txt')
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()
    return render_template('display.html', image_path=image_path, text=text)

if __name__ == '__main__':
    app.run(debug=True)
