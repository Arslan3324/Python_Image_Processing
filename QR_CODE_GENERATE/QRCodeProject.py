# # this peice of code generate QRCODE
# import qrcode
# from PIL import  Image

# generate_image = qrcode.make("Abdul Jabbar - 4520307529424")
# generate_image.save('image3.png')

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import simpleaudio 

#img = cv2.imread('image1.png')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

wave_obj = simpleaudio.WaveObject.from_wave_file("beepone.wav")
wave_obj1 = simpleaudio.WaveObject.from_wave_file("beeptwo.wav")


with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()


while True:

    success, img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        if myData in myDataList:
            Output = myData + " Verified"
            play_obj = wave_obj.play()
            play_obj.wait_done()
        else:
            Output = "UnAuthorized"
            play_obj = wave_obj1.play()
            play_obj.wait_done()
        #detect QR
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)

        pts2 = barcode.rect
        cv2.putText(img,(Output),(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,0),2)



    cv2.imshow('Result',img)
    cv2.waitKey(1)



