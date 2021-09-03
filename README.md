# readme
### This is a readme for "Virtual Drawing Pad Project"
#### We will call it VDP henceforth.

##### task: to create a virtual drawing pad that identifies the object referred to as "stylus" and records it co-ordinates for drawing on a canvas.

**Note: all the extra addition to the code are mentioned in the comments wriiten for the code** 

To create a drawing space 
1. create an image (preferably of the same dimension of the frame)
2. capture the camera for frames
3. convert the frame to hsv from bgr
4. threshold the hsv image with the necessary values. this thresholded image is referred to as "mask"
5. apply closing on the mask and so that the noise inside the mask of the object is reduced
6. dilation is applied multiple times so that we get continuos shade inside the boundary if the object
7. we find contour of this final binary image
8. as there is may be some noise we record the index of the largest contours, assuming that contour area is always less than the object's contour area
9. find the moments of the contour with max area
10. hence find the centroid
11. draw a line with the condition that the difference between the end coordinates is not more than 50. (because of this condition nothing is drawn in the first iteration as value of ncx and ncy are set to be very large, this is important because it reduces the repition of code. if we try to remove this the number of lines of code increase by a huge number as compared to now. this is a worthy trade off and convinient. problems cause are discussed below)
12. the value of the present centroid coordinated are recorded for drawing the next line.
13. an optional if statement is inserted that says if the letter 'a'is pressed the canvas is cleared
14. last thing is to display the canvas and the frame
15. release capture and destroy all windows if escape is pressed

what happens if ncx = ncy = 23000 is not done?
>then the code while loop until drawing the line must be copied and pasted above the while loop inside a while loop with the condition that at least one contour is found so that we have value of ncx and ncy and now we can proceed to the next while loop.
>advantage of not doing this is it reduces the number of lines of codes greatly. Also, addition of all these lines of code still won't give remarkable benefit at all.

Check out the video of the working of the program

[https://drive.google.com/file/d/1uwVb0sshJlow62FZER2j-WEKrpm5E0hy/view?usp=sharing](https://)

### Contributors

#### Aditya Jivoji
