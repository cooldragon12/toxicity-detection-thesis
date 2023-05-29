from celery import shared_task
from django.core.mail import send_mail
from  .helper import read_photo, pre_gray, get_lines_needed
# @shared_task
# def read_photo_using_ocr(image):
#     image = Image.open(image)
#     pixel_values = processor(image, return_tensors="pt").pixel_values
#     generated_ids = model.generate(pixel_values)
#     generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
#     return generated_text
@shared_task
def process_image(image):
    import cv2
    image = cv2.imread(image)
    preproc= pre_gray(image)
    text = read_photo(preproc)
    lines = get_lines_needed(text)
    return lines