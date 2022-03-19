# this peice of code generate QRCODE
# import qrcode
# from PIL import  Image
#
# generate_image = qrcode.make("45203-0752942-3")
# generate_image.save('image1.png')

import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('image1.png')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
myData = ""
while True:

    success, img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        #detect QR
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)

        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)



    cv2.imshow('Result',img)
    cv2.waitKey(1)



