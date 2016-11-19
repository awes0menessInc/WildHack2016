import cv2
import time
import os

#number of frames being sent to clarifai
clarifai_fps = 5
log_time = 5
flagging = False

#select the capture device, 0 is the first, 1 is the second and so on
#Enter the name of a file to look at a already existing video file
cap = cv2.VideoCapture(0)

#initialize the codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#initialize output object
session_time = time.strftime("%d-%m-%Y")+"_"+time.strftime("%H:%M:%S")
out = cv2.VideoWriter("video_log/"+session_time+".avi",fourcc,20,(640,480))

clip_time = 0
frame_index = 0

clip_directory = ""

current_time = time.time()


#make directory for the frames from this session
if not os.path.exists("clarifai_frames/"+session_time):
    os.makedirs("clarifai_frames/"+session_time)

if not os.path.exists("flagged_clips/"+session_time):
    os.makedirs("flagged_clips/"+session_time)




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
        cv2.imwrite("clarifai_frames/"+session_time+"/frame"+"_"+str(frame_index)+"_"+new_time_str+".png",frame)
        current_time = time.time()
        frame_index +=1


    if(new_time-clip_time <= log_time):
        flagging = True
        print(new_time-clip_time)
        print("writing frame")
        clip.write(frame)
    else:
        flagging = False



    #break loop if q pressed
    k = cv2.waitKey(1)&0xFF
    if k == ord('q'):
        break
    #REPLACE 'k == ord('f')' with clarfai identifying abnormalities
    if k == ord('f') and not flagging:
        clip_time = time.time()
        clip_time_str = str(new_time).replace(".","")
        clip_directory = "flagged_clips/"+session_time+"/clip_"+clip_time_str+".avi"
        clip = cv2.VideoWriter(clip_directory,fourcc,20,(640,480))

cap.release()
out.release()
cv2.destroyAllWindows()



    #clip_index +=1
