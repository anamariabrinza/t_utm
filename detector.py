import cv2
import sqlite3
from datetime import datetime

import serial
#ser = serial.Serial('COM3', 9600, timeout=0)



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainingData.yml')
faceCascade = cv2.CascadeClassifier('D:/UTM/teza/lib/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt2.xml')
path = 'dataset'

def getProfile(id):
    connect = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Students WHERE ID = " + str(id)
    cursor = connect.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    connect.close()
    return profile

def RegisterData(time, pID):
    connect = sqlite3.connect("FaceBase.db")
    c = connect.cursor()
    c.execute("INSERT INTO Identification(Time, PersonID) VALUES(?,?)", (time, pID))
    connect.commit()
    connect.close()

#cap = cv2.VideoCapture("rtsp://192.168.55.204/video.mp4")
# crearea uneui parametru/var pe langa cap care ar defini id-ul camerei

#second camera
cap2 = cv2.VideoCapture(0) #('D:/FAF ONG/MOV_0548.mp4') #('D:/Microlab/for movie/MVI_2414.MOV') #(0)


font = cv2.FONT_HERSHEY_SIMPLEX
color = (255,255,255)
stroke = 2

def getPerson(im):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in faces:
        id, conf = recognizer.predict(gray[y:y + h, x:x + w])

        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 1)
        print(conf)
        if conf <= 55:  # < 55: #>= 45 and conf <= 85: #((100 - float(conf)) <= 50):
            profile = getProfile(id)
            if id:

                if (profile != None):
                    print(profile[0])
                    print(str(datetime.now()))
                    print("------")
                    RegisterData(datetime.now(), profile[0])

                    #var = '1'.encode('utf-8')  # input("Enter 0 or 1 to control led: ")
                    #ser.write(var)

                    cv2.putText(im, str(profile[1]), (x, y), font, 1, color, stroke, cv2.LINE_AA)
                    #               cv2.putText(im, profile[2], (x, y2), font, 1, color, stroke, cv2.LINE_AA)
                    #               cv2.putText(im, profile[3], (x, y3), font, 1, color, stroke, cv2.LINE_AA)
            else:
                cv2.putText(im, "Unknown", (x, y), font, 1, color, stroke, cv2.LINE_AA)
        #else:
         #   var = '2'.encode('utf-8')  # input("Enter 0 or 1 to control led: ")
          #  ser.write(var)
count = 0
while (True):
    #ret, im1 = cap.read()
    ret2, im2 = cap2.read()
   # cap.set(cv2.CAP_PROP_FPS, 1)
    #getPerson(im1)
    getPerson(im2)

    #if (ret == True):
     #   break

    #if count % 10 == 0:
       # cv2.imwrite('frame%d.jpg' % count, image)
    #cv2.imshow('IP camera', im1)
    cv2.imshow('Laptop Camera', im2)
    #count += 1

   # cv2.waitKey(1) #work on it si la flux video


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release handle to the webcam
#cap.release()
cap2.release()
cv2.destroyAllWindows()
