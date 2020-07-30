#face detection program


import cv2
cap=cv2.VideoCapture(0) #opens the inbuilt web cam when we pass the paramter 0
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #classifier file which has all the features of human face
while True:
    ret,frame=cap.read() #ret detects if the frame is true or false and frame returns the picture
    if ret==True:
        images=classifier.detectMultiScale(frame) #classifies the face
        for image in images:
            x,y,w,h=image #taking out dimensions of the graphical plot that for the face part
            if w>150 and h>100: #setting the threshold
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3) #crops the face here the 3rd parameter is the bgr value and the last paramter is the thickness
        cv2.imshow("Image",frame)
    key=cv2.waitKey(1) #changes the frame after every one millisecond
    if key==ord('q'): #closes the webcam when we press 'q'
        break
cap.release() #video closed
cv2.destroyAllWindows()#destroys all the running windows






