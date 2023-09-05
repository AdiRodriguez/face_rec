import cv2
import numpy as np
import os
from time import sleep

names = ['None',]

id = 0
# names related to ids: The names associated to the ids: 1 for Mohamed, 2 for Jack, etc...
# add a name into this list
#Video Capture

def log_in():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    
    face_cascade_Path = "haarcascade_frontalface_default.xml"


    faceCascade = cv2.CascadeClassifier(face_cascade_Path)

    font = cv2.FONT_HERSHEY_SIMPLEX

    names
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    # Min Height and Width for the  window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    keep_going = True
    while keep_going:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                print(f"Sign in Successful! Welcome: {id}")
                keep_going = False
            else:
                # Unknown Face
                id = "Who are you ?"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)
        # Escape to exit the webcam / program
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    cam.release()
    cv2.destroyAllWindows()
