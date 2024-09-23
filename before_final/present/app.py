import gradio as gr
import pytesseract
from PIL import Image
from difflib import SequenceMatcher

# ฟังก์ชันสำหรับการจับคู่ข้อความที่ดีที่สุด
def get_best_alignment(ref, ocr):
    matcher = SequenceMatcher(None, ref, ocr)
    matches = matcher.get_opcodes()
    return matches

# ฟังก์ชันสำหรับการประเมินการจับคู่ข้อความ
def evaluate_alignment(matches, ref, ocr):
    correct_chars = 0
    incorrect_chars = 0
    errors = []
    correct_details = []

    ref_chars = list(ref)
    ocr_chars = list(ocr)

    for tag, i1, i2, j1, j2 in matches:
        if tag == 'equal':
            correct_chars += (i2 - i1)
            for i in range(i1, i2):
                correct_details.append((i, ref_chars[i]))
        else:
            incorrect_chars += max(i2 - i1, j2 - j1)
            for i in range(i1, i2):
                expected_char = ref_chars[i]
                got_char = ocr_chars[j1 + (i - i1)] if j1 + (i - i1) < len(ocr_chars) else 'None'
                errors.append((i, expected_char, got_char))


    return correct_chars, incorrect_chars, errors, correct_details #,  edit_distance


# ฟังก์ชันสำหรับประมวลผล OCR
def ocr_process(image, reference_text_file=None):
    # แปลงภาพเป็นสีเทาเพื่อเพิ่มความแม่นยำในการ OCR
    gray_image = image.convert('L')

    # กำหนดค่าการใช้งาน Tesseract OCR
    custom_config = r'--tessdata-dir "/Users/gunnviryasiri/pythainlp-data/tessdata" --oem 1 --psm 3'
    ocr_text = pytesseract.image_to_string(gray_image, config=custom_config, lang='tha+eng')

    # จัดรูปแบบผลลัพธ์ที่ได้จาก OCR
    processed_ocr_text = "\n".join([line for line in ocr_text.splitlines() if line.strip()])

    # ถ้ามีไฟล์เปรียบเทียบ
    if reference_text_file is not None:
        try:
            # อ่านเนื้อหาจากไฟล์ที่ส่งเข้ามา
            reference_text = reference_text_file.name  # ใช้ .name แทน .read()
            with open(reference_text, 'r', encoding='utf-8') as f:
                reference_text = f.read().replace("\n", "")
                
            processed_ocr_text_cleaned = processed_ocr_text.replace(" ", "").replace("\n", "")
            reference_text_cleaned = reference_text.replace(" ", "").replace("\n", "")

            # เรียกใช้ฟังก์ชันประเมินผลลัพธ์
            matches = get_best_alignment(reference_text_cleaned, processed_ocr_text_cleaned)
            correct_chars, incorrect_chars, errors, correct_details = evaluate_alignment(matches, reference_text_cleaned, processed_ocr_text_cleaned)

            total_chars = len(reference_text_cleaned)
            precision = (correct_chars / (correct_chars + incorrect_chars)) * 100 if (correct_chars + incorrect_chars) > 0 else 0
            recall = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
            accuracy = correct_chars / total_chars if total_chars > 0 else 0

            #             # สร้างข้อความที่มีเปอร์เซ็นต์
            # accuracy_str = f"{round(accuracy, 2)}%"
            # precision_str = f"{round(precision, 2)}%"
            # recall_str = f"{round(recall, 2)}%"

            return processed_ocr_text, accuracy * 100, precision, recall

        except FileNotFoundError:
            return processed_ocr_text, None, None, None
    else:
        # หากไม่มีไฟล์เปรียบเทียบ จะแสดงแค่ผล OCR
        return processed_ocr_text, None, None, None


# theme = gr.themes.Monochrome(
#     primary_hue="sky",
#     secondary_hue="blue",
#     neutral_hue="stone",
#     radius_size="md",
# ).set(
#     background_fill_primary='*primary_50',
#     background_fill_primary_dark='*secondary_950',
#     background_fill_secondary='*secondary_300',
#     background_fill_secondary_dark='*neutral_700',
#     border_color_accent='*primary_900',
#     button_primary_background_fill='*secondary_600',
#     button_primary_background_fill_hover='*secondary_700',
#     button_primary_background_fill_hover_dark='*primary_600',
#     button_primary_border_color_hover_dark='*secondary_600',
#     button_primary_text_color_hover_dark='*secondary_100'
# )

theme = gr.themes.Monochrome(
    primary_hue="yellow",
    secondary_hue="blue",
    neutral_hue="cyan",
    radius_size="sm",
).set(
    background_fill_primary='*primary_100',
    background_fill_primary_dark='*secondary_950',
    background_fill_secondary_dark='*neutral_950',
    background_fill_secondary='*neutral_200',
)

#  # # คำนวณ Edit Distance
# edit_distance = sum([max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in matches if tag != 'equal'])

# ฟังก์ชันสำหรับรัน Gradio UI
def run_gradio():
    interface = gr.Interface(
        theme=theme,
        fn=ocr_process,
        inputs=[
            gr.Image(type="pil", label="Upload Image"),  # อัปโหลดภาพสำหรับทำ OCR
            gr.File(label="Upload Reference Text File (.txt)")  # เพิ่มไฟล์ .txt สำหรับการเปรียบเทียบ
        ],
        outputs=[
            gr.Textbox(label="OCR Result"),
            gr.Number(label="Accuracy (if evaluated)"),
            gr.Number(label="Precision (if evaluated)"),
            gr.Number(label="Recall (if evaluated)")# ,
            # gr.Number(label="edit distance (if evaluated)")
        ],
        title="OCR with Optional Evaluation",
        description="Upload an image for OCR. Optionally, upload a .txt file for evaluation."
    )
    
    # เริ่มการทำงานของ Gradio
    interface.launch()

# เรียกใช้ Gradio
if __name__ == "__main__":
    run_gradio()
