import cv2
import numpy as np

cap = cv2.VideoCapture("eye_recording.flv")


while True:
    ret, frame = cap.read()
    roi = frame[269: 795, 537:1416] #to crop the frame
    roi_g = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) #convert to black and white
    roi_g = cv2.GaussianBlur(roi_g, (7, 7), 0) #removing the noise

    _, threshold = cv2.threshold(roi_g, 5, 255, cv2.THRESH_BINARY_INV)#threshold
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True) #sorting function reversed for descending order   

    for cnt in contours:
            cv2.drawContours(roi, [cnt], -1, (0,0,255), 2)
            print(contours)
            break # the break is added to stop drawing after the first(biggest) contour

    cv2.imshow("threshold", threshold)
    cv2.imshow("Black and white", roi_g)
    cv2.imshow("ROI", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows() #this function will automatically close all the windows.

