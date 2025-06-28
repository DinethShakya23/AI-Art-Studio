import cv2
import os
import time
import numpy as np
# import moduleFingerTracking as mtf

folderPath = "images"
imageList = os.listdir(folderPath)  # path to images
print(imageList)

overlayList = []  # list to store images 
for impath in imageList:
    image = cv2.imread(f'{folderPath}/{impath}')
    overlayList.append(image)

header = overlayList[0]

capture = cv2.VideoCapture(0) #useing the webcam
capture.set(3,1288)    #frame width to 1288 pixels
capture.set(4,720)     #frame height to 720 pixels

if not capture.isOpened():
    print("Error: Could not open webcam or evernal camera.")
    exit()


while True:
    success, frame = capture.read()
    if not success:
        print("Ignoring empty camera frame.")
        break
    cv2.imshow("Webcam", frame)    # show the current frame from the webcam or exernam camera
    cv2.waitKey(1)                 # this will keep the display window (cv2.imshow) responsive & allow the window to refresh with each new frame.