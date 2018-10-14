import os
import cv2
import numpy as np
from PIL import Image

face_cascade = cv2.CascadeClassifier('D:/UTM/teza/lib/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer = cv2.LBPHFaceRecognizer_create()
path = 'dataset'

def getImagesWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        print(os.path.split(imagePath)[-1].split(".")[1])
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)
        IDs.append(ID)
        #cv2.imshow("training", faceNp)
        #cv2.waitKey(10)
    return IDs, faces

Ids, faces = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()