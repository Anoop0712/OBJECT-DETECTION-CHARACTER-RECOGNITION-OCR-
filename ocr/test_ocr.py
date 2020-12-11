# This is a sample Python script.

#import opencv,numpy and Pytesseract library
import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

##for Execution of methods I used the installed pytesseract-ocr.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Read example/input image
img = cv2.imread('R.png')
#this color change from BGR2RGB is due to pytesseract only uses RGB values
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#############################################
#### Detecting Characters  ######
#############################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
    cv2.putText(img, b[0], (x, hImg - y+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)


cv2.imshow('img', img)
cv2.waitKey(0)



##############################################
##### Image to String   ######
##############################################
# print(pytesseract.image_to_string(img))


##############################################
##### Detecting Words  ######
##############################################
# boxes = pytesseract.image_to_data(img)
# for a,b in enumerate(boxes.splitlines()):
#         print(b)
#         if a!=0:
#             b = b.split()
#             if len(b)==12:
#                 x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#                 cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
#                 cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
#
#
# cv2.imshow('img', img)
# cv2.waitKey(0)