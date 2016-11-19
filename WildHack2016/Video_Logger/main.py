import cv2
import time
import os

#number of frames being sent to clarifai
clarifai_fps = 5

#select the capture device, 0 is the first, 1 is the second and so on
#Enter the name of a file to look at a already existing video file
cap = cv2.VideoCapture(0)

#initialize the codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#initialize output object
session_time = time.strftime("%d-%m-%Y")+"_"+time.strftime("%H:%M:%S")
out = cv2.VideoWriter("video_log/"+session_time+".avi",fourcc,20,(640,480))

index = 0;

current_time = time.time()

#make directory for the frames from this session
if not os.path.exists("clarifai_frames/"+session_time):
    os.makedirs("clarifai_frames/"+session_time)

while True:

    #ret is a boolean and frame is the frame
    ret,frame = cap.read()

    #write the frame to the file
    out.write(frame)

    #show the image (the frame)
    cv2.imshow("frame",frame)
    new_time = time.time()

    #save frames at the rate of the fps specified
    if(new_time-current_time >= 1.0/clarifai_fps):

        new_time_str = str(new_time).replace(".","")

        cv2.imwrite("clarifai_frames/"+session_time+"/frame"+"_"+str(index)+"_"+new_time_str+".png",frame)

        current_time = time.time()
        index +=1

    #break loop if q pressed
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
