import cv2
import sqlite3

faceDetect = cv2.CascadeClassifier('D:/UTM/teza/lib/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) #("rtsp://192.168.55.204/video.mp4") #("rtsp://192.168.55.201/video.mp4")

def insertOrUpdate(Id, Name):
    connect = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Students WHERE ID = " + str(Id)
    cursor = connect.execute(cmd)
    isRecordExists = 0
    for row in cursor:
        isRecordExists = 1
    if(isRecordExists==1):
        cmd = "UPDATE Students SET Name= " + str(Name) + "WHERE ID= "+ str(Id)
    else:
        cmd = "INSERT INTO Students(ID, Name) Values(" + str(Id) + "," + str(Name) + ")"
    connect.execute(cmd)
    connect.commit()
    connect.close()
id = input('Enter the id: ')
name = input('Enter the name: ')
insertOrUpdate(id, name)

sampleNum = 0

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for(x,y,w, h) in faces:
        sampleNum +=1
        cv2.imwrite("dataset/User." +str(id) + "." + str(sampleNum) + ".jpg", gray[y:y+h, x: x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.waitKey(300)
    cv2.imshow("Face", img)

    cv2.waitKey(10);
    if (sampleNum>50):
        break
cap.release()
cv2.destroyAllWindows()