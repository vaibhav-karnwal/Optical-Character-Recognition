import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img=cv2.imread('imgtotext.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))
