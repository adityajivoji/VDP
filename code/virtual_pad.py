#importing requiered libraries
import cv2 as cv
import numpy as np
img = np.zeros((480, 640, 3), np.uint8) #creating an image which is the drawing space
cv.bitwise_not(img,img)                 #turning all the zeros to 1s so that drawing pad is white(optional)
cp = np.copy(img)                       #copying this image to clear the drawing canvas(optional)
cap = cv.VideoCapture(0 + cv.CAP_DSHOW) #capturing video (+ cv.CAP_DSHOW is only used if using only 0 doesn't work)
#these are the lower and upper limits of hsv values identified create a mask of stylus
lh = 158
ls = 101
lv = 90
uh = 179
us = 255
uv = 255
lower_red = np.array([lh, ls, lv])      #creating the array for hsv thresholding
upper_red = np.array([uh, us, uv])
kernel = np.ones((3, 3), np.uint8)      #this is the kernel for passing while "closing" and dilation
ncx = ncy=  2300000                     #assigning these value so that there is no condition check everytime for 1st and2nd iteration
key = 0                                 #condition for entering into the loop
while key != 27:                        #comes out of the program when escape is pressed
    _, fram = cap.read()                #reading the camera
    frame = cv.flip(fram, 1)            #flipping the camera along the vertical axis
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  #converting frame from bgr to hsv
    mask = cv.inRange(hsv, lower_red, upper_red)    #hsv thresholding
    if (mask[:] == 255).any():                  #if there is object in the mask at least 1 white spot will be there only then proceed to find contours
        #applying closing operation on mask to remove noise from the image
        closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel) 
        #dilation is done to remove some of the dark spot inside the mask
        dilation_after_closing = cv.dilate(closing,kernel,iterations = 3)
        contours, _ = cv.findContours(dilation_after_closing, 1, 2) #detecting contours
        areas = [cv.contourArea(c) for c in contours]   #finding areas of all the contourand putting them in a list
        #finding the index of the largest contour in the above list
        cnt=contours[np.argmax(areas)]
        #using the contour with larget area to draw it on the original frame
        cv.drawContours(frame, [cnt], 0, (0,255,0), 3)
        M = cv.moments(cnt)                             #finding moments and centroid of the largest contour
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        """this condition helps draw lines that are only of a certain length so that greater differnces are ignored
        here in the first iteration nothing is drawn because ncx and ncy have very large values.
        check more information in readme"""
        if(abs(ncx-cx) < 50 and abs(ncy-cy) < 50):
            cv.line(img,(cx,cy),(ncx,ncy),(0,0,0),3)
        #copying the values of the old coordinated for the end points of next line
        ncx = cx
        ncy = cy
    cv.imshow('Drawing',img)        #displaying the drawing pad
    key = cv.waitKey(1)             #waiting for one millisecond for some input from the user
    if key == 97:                   #if the user gave 'a' as the input the the canvas is cleared(optional)
        img = np.copy(cp)
    cv.imshow("Frame",frame)        #displaying the frame with largest controur drawn on it
#releasing the capture and destroying all the windows
cap.release()
cv.destroyAllWindows()
