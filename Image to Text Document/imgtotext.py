import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(r'C:\Users\Er Vaibhav Karnwal\Desktop\Image to Text Document\imgtotext.png'))