import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

cv2.setUseOptimized(True)


def add_value_list(number_frame,list):
    if number_frame not in list:
        list.append(number_frame)


def add_value_tup_list(number_frame,number_peaple,list,list_tup):
    if number_frame not in list:
        list.append(number_frame)
        tup = (number_frame,number_peaple)
        list_tup.append(tup)

#Renomear funçao
def average_person_frame(list_tup):
    #print(" len of the list  ",list_tup.__len__())
    among_peaple = 0
    average = 0

    for indx, elem in enumerate(list_tup):
        if(indx > 0):
          # print("index :",indx)
           #print("number of peaple by frame :",elem[1])
           among_peaple = among_peaple + elem[1]

    #average = among_peaple /  list_tup.__len__()
    return among_peaple


def animate(i):
    graph_data = faces_found_frame[1:]

    xs = []
    ys = []
    for indx, elem in enumerate(graph_data):

            xs.append(elem[0])
            ys.append(elem[1])
    ax1.clear()
    ax1.plot(xs,ys)
    # X IS THE FRAMES AND 'Y' IS THE PEOPLE IN THE VIDEO - ON THE GRAPH






face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture('video-file.mp4')

property_id = int(cv2.CAP_PROP_FRAME_COUNT)
length = int(cv2.VideoCapture.get(cap, property_id))
framerate = cap.get(cv2.CAP_PROP_FPS)
print("total of frames: "+str(length))
print("FPS: "+str(framerate))

count_next_frame = 0

count_frame_current = 0



porcentage_faces_video = 0
list_of_faces_found = []


#question 3 -  What is the average amount of faces in a frame with at least one face
faces_found_frame = [()]   #usar esta lista no math plot
faces_found_indx = []

#Question 4
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


#Question 2 - What is the average amount of faces in a frame?



#2518
while count_frame_current <  2518:

    ret, img = cap.read()
    count_next_frame = count_next_frame + 1


    if (count_next_frame % 25.0 == 0 ):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      #  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        count_frame_current = count_frame_current +1

        #number_someone_frame = number_someone_frame + 1

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
           # print("number of faces "+str( faces.shape[0]))


            #question 3 -  What is the average amount of faces in a frame with at least one face
            if (faces.shape[0] > 0):
                add_value_tup_list(number_frame=count_frame_current, number_peaple=faces.shape[0] , list=faces_found_indx, list_tup=faces_found_frame)



            # question 1 any Question - mostra a porcentagem onde somente um rosto aparece no video
            if (faces.shape[0] == 1):
                add_value_list(count_frame_current,list_of_faces_found)


        porcentage_faces_video =  len(list_of_faces_found) / count_frame_current


        cv2.imshow('img', img)


    k = cv2.waitKey(30) & 0xFF
    if k==27:
        break


#Questiom 1
print(" What’s the percentage of time a face is shown in the video? % ",porcentage_faces_video*100)

#QUESTION 3
print("number of peaple: "+str(average_person_frame( list_tup=faces_found_frame)))
print("Total frames: ",count_frame_current)

print(" What is the average amount of faces in a frame with at least one face ?" + str( average_person_frame( list_tup=faces_found_frame) / len(faces_found_indx)))




#Question 2
print(" What is the average amount of faces in a frame?" + str( average_person_frame( list_tup=faces_found_frame) / count_frame_current ))

#Question 4
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
# X IS THE FRAMES AND 'Y' IS THE PEOPLE IN THE VIDEO - ON THE GRAPH
#plt.close(fig)

cap.release()
cv2.destroyAllWindows()

